
class Remindr(object):
    def __init__(self, phone, recording, calendar, cron):
        self.phone = phone
        self.recording = recording
        self.calendar = calendar
        self.cron = cron

    def save(self):
        assert False


class PhoneNumber(object):
    def __init__(self, number):
        self.number = number


class Cron(object):
    def __init__(self, schedule_string):
        self.schedule_string = schedule_string


class AzureStorageObject(object):
    def __init__(self):
        pass

    def savedObject(self, ocket):
        pass


class AzureFunctions(object):
    def __init__(self):
        pass

    def add_item(self, audio, phone_number, cron):
        pass


class Polly(object):
    def __init__(self, location):
        pass

    def recording(self, location):
        pass