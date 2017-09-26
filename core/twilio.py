import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


class TwilioPhone(object):
    def __init__(self, phone_number):
        self._phone_number = phone_number
        self._account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self._auth_token = os.environ['TWILIO_AUTH_TOKEN']

    def call(self, url):
        client = Client(self._account_sid, self._auth_token)
        number = client.api.account.incoming_phone_numbers.create(
            voice_url=url,
            phone_number=self._phone_number
        )
        return number.sid

    def is_valid(self):
        try:
            client = Client(self._account_sid, self._auth_token)
            response = client.lookups.phone_numbers(self._phone_number).fetch(type="carrier")
            return True

        except TwilioRestException as e:
            if e.code == 20404:
                return False
            else:
                raise e
