class FakeRemindr(object):
    def __init__(self, phone, message, cron):
        self.phone = phone
        self.message = message
        self.cron = cron


class FakeStorage(object):
    def __init__(self):
        self.ockets = []

    def save(self, ocket):
        self.ockets.append(ocket)

    def ockets(self):
        return self.ockets


class FakeSchedule(object):
    def __init__(self):
        self.items = []

    def add_item(self, audio, phone_number, cron):
        self.items.append(cron)
        pass

    def items(self):
        return self.items


class FakeAudio(object):
    def __init__(self, location):
        pass

    def recording(self, location):
        self.synthesize_speech_was_called = True