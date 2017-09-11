import os
import uuid
from unittest import TestCase
from core.objects import *
from core.fakes import *

class TestRemindr(TestCase):
    def test_attributes(self):
        remindr = Remindr('123-123-1234', 'location', 'everyday')
        assert '123-123-1234' == remindr._phone
        assert 'location' == remindr._recording
        assert 'everyday' == remindr._cron

    def test_save(self):
        remindr = Remindr(
                    PhoneNumber('123-132-1234'),
                    FakeStorageObject(
                        FakeAudio('message')
                    ),
                    Cron('* * * *')
                )

        function_processor = FakeProcessor()
        function_processor.add_item(remindr)

        assert len(function_processor.items) > 0

class TestPolly(TestCase):
    def test_recording(self):
        polly = Polly('this is a message')
        mp3 = polly.recording()
        assert mp3

class TestS3Object(TestCase):
    def test_url(self):

        test_bucket_name = 'test-remindrs'
        test_file_name = 'test-remindr.mp3'
        test_key = str(uuid.uuid4())

        with open(test_file_name, 'w') as file:
            file.truncate(1024)

            s3_object = S3Object(test_bucket_name, test_file_name, test_key)
            url = s3_object.url()
            assert url

            test_url = 'https://s3.us-east-1.amazonaws.com/{0}/{1}'.format(test_bucket_name, test_key)
            assert url == test_url

            s3_object.delete()
            file.close()
            os.remove(test_file_name)

        assert not os.path.exists(test_file_name)