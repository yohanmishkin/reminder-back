class Remindr(object):
    def __init__(self, phone, recording, cron):
        self._phone = phone
        self._recording = recording
        self._cron = cron


class PhoneNumber(object):
    def __init__(self, number):
        self._number = number


class Cron(object):
    def __init__(self, schedule_string):
        self._schedule_string = schedule_string


class AWSLambda(object):
    def __init__(self):
        pass

    def add_item(self, audio, phone_number, cron):
        pass
