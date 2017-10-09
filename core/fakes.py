class FakeStorageObject(object):
    def __init__(self, bucket_name, file_name):
        self._bucket_name = bucket_name
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
    def __init__(self, message):
        self.message = message

    def recording(self, file_name):
        return file_name


class InvalidPhone(object):
    def call(self, url):
        raise Exception('Invalid phone number')
