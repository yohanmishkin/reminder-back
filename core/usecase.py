
class Usecase(object):
    def __init__(self, storage_object, phone, payment):
        self._storage_object = storage_object
        self._phone = phone
        self._payment = payment

    def run(self):
        self._phone.call(
            self._storage_object.url()
        )

        self._payment.charge(
            100,
            "usd",
            "one reminder"
        )
