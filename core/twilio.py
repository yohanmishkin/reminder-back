import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException


class TwilioPhone(object):
    def __init__(self, phone_number):
        self._phone_number = phone_number

    def is_valid(self):
        try:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']

            client = Client(account_sid, auth_token)
            response = client.lookups.phone_numbers(self._phone_number).fetch(type="carrier")
            return True

        except TwilioRestException as e:
            if e.code == 20404:
                return False
            else:
                raise e
