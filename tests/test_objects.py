from unittest import TestCase
from core.objects import Remindr

class TestRemindr(TestCase):
    def test_attributes(self):
        remindr = Remindr(1234, 'message', 'cron')
        assert 1234 == remindr.phone
        assert 'message' == remindr.message
        assert 'cron' == remindr.cron