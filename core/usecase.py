import os
import uuid
import stripe

from core.polly import Polly
from core.s3 import S3Object
from core.twilio import TwilioPhone


class Usecase(object):

    def __init__(self, message, phone_number, token):
        self._message = message
        self._phone_number = phone_number
        self._token = token

    def run(self):

        TwilioPhone(self._phone_number).call(
            S3Object(
                os.environ['AUDIO_BUCKET'],
                Polly(self._message).recording(
                    '{0}.mp3'.format(str(uuid.uuid4()))
                )
            ).url()
        )

        stripe.api_key = os.environ['STRIPE_KEY']

        stripe.Charge.create(
            amount=100,
            currency="usd",
            description="One reminder",
            source=self._token,
        )
