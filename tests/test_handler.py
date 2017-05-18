from unittest import TestCase
from core.objects import Remindr, Cron, PhoneNumber
from core.handler import Handler
from core.fakes import FakeAudio, FakeStorageObject, FakeSchedule

class TestHandler('''TestCase'''):
    def test_run(self):
        
        event = {
            'message': 'Hello',
            'phone': '123-123-1234',
            'cron': '* * * *'
        }

        handler.run(event)