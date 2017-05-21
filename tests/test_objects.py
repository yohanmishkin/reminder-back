from unittest import TestCase
from core.objects import *
from core.fakes import *

class TestRemindr(TestCase):
    def test_attributes(self):
        remindr = Remindr('123-123-1234', 'location', FakeProcessor(), 'everyday')
        
        assert '123-123-1234' == remindr.phone
        assert 'location' == remindr.recording
        assert remindr.processor
        assert 'everyday' == remindr.cron

    def test_save(self):
        remindr = Remindr(
                    PhoneNumber('123-132-1234'),
                    FakeStorageObject(
                        FakeAudio('message')
                    ),
                    FakeProcessor(),
                    Cron('* * * *')
                )

        remindr.save()
        assert len(remindr.processor.items) > 0
