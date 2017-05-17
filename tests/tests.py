from unittest import TestCase

from doubles import allow

from core.models import Remindr, S3, Schedule, Audio
from core.handler import RemindrFunction


class TestRemindr(TestCase):
    def test_remindr_properties(self):
        remindr = Remindr(1234, 'message', 'cron')
        self.assertEqual(1234, remindr.phone)
        self.assertEqual('message', remindr.message)
        self.assertEqual('cron', remindr.cron)


class TestHandler(TestCase):
    def test_handler_run(self):
        fake_audio = Audio('text.mp3')
        allow(fake_audio).recording.and_return('text.mp3')

        fake_storage = S3()
        # allow(fake_storage).savedObject

        fake_schedule = Schedule()
        # allow(fake_schedule).add_item

        handler = RemindrFunction(fake_audio, fake_storage, fake_schedule)

        event = {
            'message': 'Hello',
            'phone': '123-123-1234',
            'cron': '* * * *'
        }

        handler.run(event)