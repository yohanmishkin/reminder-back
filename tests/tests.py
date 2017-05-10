from mock import mock
from unittest import TestCase
from core.models import Remindr
from core.handler import RemindrFunction


class TestRemindr(TestCase):
    def test_remindr_properties(self):
        remindr = Remindr(1234, 'message', 'cron')
        self.assertEqual(1234, remindr.phone)
        self.assertEqual('message', remindr.message)
        self.assertEqual('cron', remindr.cron)

class TestHandler(TestCase):
    def test_handler_run(self):
        fake_audio = mock.Mock()
        fake_audio.recording.returns = 'text.mp3'

        fake_storage = mock.Mock()
        fake_storage.save.returns = None

        fake_scheduler = mock.Mock()
        fake_scheduler.schedule.returns = None

        handler = RemindrFunction(fake_audio, fake_storage, fake_scheduler)

        event = {
            'message': 'Hello',
            'phone': '123-123-1234',
            'cron': '* * * *'
        }

        handler.run(event)

        self.assertTrue(fake_audio.recording.called)
        self.assertTrue(fake_storage.savedObject.called)
        self.assertTrue(fake_scheduler.schedule.called)