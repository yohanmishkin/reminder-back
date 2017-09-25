import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

class TwilioPhone(object):
    def __init__(self, phone_number):
        self._phone_number = phone_number

    # Your Account Sid and Auth Token from twilio.com/user/account
    # Store them in the environment variables:
    # "TWILIO_ACCOUNT_SID" and "TWILIO_AUTH_TOKEN"

    def is_valid(self):
        try:
            ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
            AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            response = client.lookups.phone_numbers(self._phone_number).fetch(type="carrier")
            return True
        except TwilioRestException as e:
            if e.code == 20404:
                return False
            else:
                raise e
