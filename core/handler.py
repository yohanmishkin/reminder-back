import urllib.parse
import uuid
import sys
import os
import stripe
from core.objects import S3Object, Polly
from core.twilio import TwilioPhone

stripe.api_key = os.environ['STRIPE_KEY']
RECORDINGS_BUCKET = os.environ['AUDIO_BUCKET']


def charge(event, context):
    try:
        email, message, token, phone_number, cron = unpack_data(event)

        TwilioPhone(phone_number).call(
            S3Object(
                RECORDINGS_BUCKET,
                Polly(message).recording(
                    '{0}.mp3'.format(str(uuid.uuid4()))
                )
            ).url()
        )

        stripe.Charge.create(
            amount=100,
            currency="usd",
            description="One reminder",
            source=token,
        )

        response = {
            "statusCode": 200,
            "body": "Scheduled call and charged card"
        }

        return response

    except:
        exception = sys.exc_info()[0]
        return {
            "statusCode": 500,
            "body": exception
        }


def unpack_data(event):
    encoded_form = urllib.parse.unquote(event['body'])
    decoded_form = urllib.parse.parse_qs(encoded_form)
    token = decoded_form["token"][0]
    email = decoded_form["email"][0]
    message = decoded_form["message"][0]
    phone = decoded_form["phone"][0]
    cron = decoded_form["cron"][0]

    return email, message, token, phone, cron
