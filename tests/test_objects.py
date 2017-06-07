from tempfile import TemporaryFile
from unittest import TestCase
from core.objects import *
from core.fakes import *

class TestRemindr(TestCase):
    def test_attributes(self):
        remindr = Remindr('123-123-1234', 'location', 'everyday')
        assert '123-123-1234' == remindr.phone
        assert 'location' == remindr.recording
        assert 'everyday' == remindr.cron

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
    def test_location(self):
        temp_file = TemporaryFile()
        s3 = S3Object('test-remindrs', temp_file)
        location = s3.location()
        assert location