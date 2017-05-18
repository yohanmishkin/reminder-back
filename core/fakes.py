class FakeRemindr(object):
    def __init__(self, phone, message, cron):
        self.phone = phone
        self.message = message
        self.cron = cron


class FakeS3(object):
    def __init__(self):
        pass

    def savedObject(self, ocket):
        pass


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
        pass