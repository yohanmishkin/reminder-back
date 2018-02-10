
class FakeStorageObject(object):
    def __init__(self, file):
        pass

    def save(self, ocket):
        self.ockets.append(ocket)

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

    def recording(self):
        self.synthesize_speech_was_called = True