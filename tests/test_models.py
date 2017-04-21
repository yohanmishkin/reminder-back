from unittest import TestCase
from core.models import Remindr

__author__ = 'Tommy'


class TestRemindr(TestCase):
    def test_remindr_properties(self):
        remindr = Remindr(1234)
        self.assertEqual(1234, remindr.phone)
