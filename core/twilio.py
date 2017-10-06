import os
from xml.etree.ElementTree import Element, SubElement, ElementTree

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


class TwilioPhone(object):
    def __init__(self, phone_number):
        self._phone_number = phone_number
        self._account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self._auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self._from = os.environ['TWILIO_FROM']

    def call(self, url):
        client = Client(self._account_sid, self._auth_token)

        call = client.api.account.calls.create(
            to=self._phone_number,
            from_=self._from,
            url=url
        )

        return call.sid

    def is_valid(self):
        try:
            client = Client(self._account_sid, self._auth_token)
            client.lookups.phone_numbers(self._phone_number).fetch(type="carrier")
            return True

        except TwilioRestException as e:
            if e.code == 20404:
                return False
            else:
                raise e


class TwimlFile(object):
    def __init__(self, file_url):
        self._file_url = file_url

    def write(self):
        top = Element('Response')
        child = SubElement(top, 'Play')
        child.text = self._file_url

        file_name = 'voice.xml'
        ElementTree(top).write(file_name)
        return file_name
