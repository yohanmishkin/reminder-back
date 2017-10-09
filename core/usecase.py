import os

import stripe


class Usecase(object):
    def __init__(self, storage_object, phone, token):
        self._storage_object = storage_object
        self._phone = phone
        self._token = token

    def run(self):
        self._phone.call(
            self._storage_object.url()
        )

        stripe.api_key = os.environ['STRIPE_KEY']

        stripe.Charge.create(
            amount=100,
            currency="usd",
            description="One reminder",
            source=self._token,
        )
