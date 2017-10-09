from unittest import TestCase

from core import Usecase
from core.fakes import InvalidPhone, FakeStorageObject, FakeAudio


class TestUsecase(TestCase):
    def test_giveninvalidnumber_throwsexception(self):
        usecase = Usecase(
            FakeStorageObject(
                'test-bucket',
                FakeAudio('message-message-message').recording('filename.mp3')
            ),
            InvalidPhone(),
            'token-token-token'
        )

        with self.assertRaises(Exception):
            usecase.run()
