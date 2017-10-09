from unittest import TestCase

from core import Usecase
from core.fakes import InvalidPhone, FakeStorageObject, FakeAudio, FakePayment, FakePhone


class TestUsecase(TestCase):
    def test_giveninvalidnumber_throwsexception(self):
        with self.assertRaises(Exception):
            Usecase(
                FakeStorageObject(
                    FakeAudio().recording('filename.mp3')
                ),
                InvalidPhone(),
                FakePayment()
            ).run()

    def test_paymentmethod_callscharge(self):
        payment = FakePayment()
        Usecase(
            FakeStorageObject(
                FakeAudio().recording('filename.mp3')
            ),
            FakePhone(),
            payment
        ).run()

        self.assertTrue(payment.charge_was_called)
        self.assertEqual(100, payment.charge_amount)
        self.assertEqual("usd", payment.charge_currency)
        self.assertEqual("one reminder", payment.charge_description)
