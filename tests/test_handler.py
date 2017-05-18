from unittest import TestCase
from core.handler import Handler
from core.fakes import FakeAudio, FakeS3, FakeSchedule

class TestHandler(TestCase):

    def test_run(self):
        fake_audio = FakeAudio('text.mp3')
        fake_storage = FakeS3()
        fake_schedule = FakeSchedule()

        handler = Handler(fake_audio, fake_storage, fake_schedule)

        event = {
            'message': 'Hello',
            'phone': '123-123-1234',
            'cron': '* * * *'
        }

        handler.run(event)
        assert len(fake_schedule.items) > 0