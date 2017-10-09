class FakeStorageObject(object):
    def __init__(self, file_name):
        self._file_name = file_name

    def url(self):
        return self._file_name


class FakeProcessor(object):
    def __init__(self):
        self.items = []

    def add_item(self, remindr):
        self.items.append(remindr)
        pass

    def items(self):
        return self.items


class FakeAudio(object):
    def __init__(self):
        pass

    def recording(self, file_name):
        return file_name


class InvalidPhone(object):
    def call(self, url):
        raise Exception('Invalid phone number')


class FakePhone(object):
    def __init__(self):
        pass

    def call(self, url):
        pass


class FakePayment(object):
    def __init__(self):
        self.charge_was_called = False

    def charge(self, amount, currency, description):
        self.charge_was_called = True
        self.charge_currency = currency
        self.charge_amount = amount
        self.charge_description = description
        return
