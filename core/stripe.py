import stripe


class StripePayment(object):
    def __init__(self, api_key, token):
        self._api_key = api_key
        self._token = token

    def charge(self, amount, currency, description):
        stripe.api_key = self._api_key

        return stripe.Charge.create(
            amount=amount,
            currency=currency,
            description=description,
            source=self._token,
        )
