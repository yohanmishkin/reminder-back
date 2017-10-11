import os
from tempfile import gettempdir
from xml.etree.ElementTree import Element, SubElement, ElementTree

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


class TwilioPhone(object):
    def __init__(self, phone_number, _from, account_sid, auth_token):
        self._phone_number = phone_number
        self._account_sid = account_sid
        self._auth_token = auth_token
        self._from = _from

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
        output_file_name = os.path.join(gettempdir(), file_name)
        ElementTree(top).write(output_file_name)
        return output_file_name
