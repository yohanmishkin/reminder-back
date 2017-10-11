import os
import uuid
from unittest import TestCase

from core import TwilioPhone, S3Object, Polly, TwimlFile
from core.stripe import StripePayment


class TestPolly(TestCase):
    def test_recording(self):
        polly = Polly('this is a message')
        file_name = 'file_name.mp3'
        mp3 = polly.recording(file_name)
        assert mp3.endswith(file_name)


class TestS3Object(TestCase):
    def test_url(self):
        test_bucket_name = 'test-remindrs'
        test_key = str(uuid.uuid4())
        test_file_name = '{0}.mp3'.format(test_key)

        with open(test_file_name, 'w') as file:
            file.truncate(1024)

            s3_object = S3Object(test_bucket_name, test_file_name)
            url = s3_object.url()
            assert url

            test_url = 'https://s3.us-east-1.amazonaws.com/{0}/{1}'.format(test_bucket_name, test_key)
            assert url == test_url

            s3_object.delete()
            file.close()
            os.remove(test_file_name)

        assert not os.path.exists(test_file_name)


class TestTwilioPhone(TestCase):
    def test_makes_call(self):
        url = 'http://demo.twilio.com/docs/classic.mp3'
        phone_number = "+15005550006"

        sid = TwilioPhone(
            phone_number,
            phone_number,
            os.environ['TWILIO_ACCOUNT_SID'],
            os.environ['TWILIO_AUTH_TOKEN']
        ).call(url)

        assert sid


class TestTwimlFile(TestCase):
    def test_write(self):
        test_key = str(uuid.uuid4())
        test_file_name = '{0}.mp3'.format(test_key)

        with open(test_file_name, 'w') as file:
            file.truncate(1024)
            twiml_location = TwimlFile(test_file_name).write()

            assert os.path.exists(twiml_location)
            os.remove(twiml_location)

        os.remove(test_file_name)


class TestStripePayment(TestCase):
    def test_charge(self):
        response = StripePayment(
            'sk_test_BQokikJOvBiI2HlWgH4olfQ2',
            'tok_mastercard',
        ).charge(
            100, 'usd', 'description'
        )

        assert response
        self.assertEqual('succeeded', response['status'])
