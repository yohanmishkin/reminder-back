from unittest import TestCase
from core.objects import Remindr

class TestRemindr(TestCase):
    def test_attributes(self):
        remindr = Remindr('123-123-1234', 'location', CALENDAR, 'everyday')
        
        assert '123-123-1234' == remindr.phone
        assert 'location' == remindr.recording
        assert remindr.calendar
        assert 'everyday' == remindr.cron

    def test_save(self):
        remindr = Remindr()
        remindr.save()
        
        assert len(remindr.calendar.items) > 0
