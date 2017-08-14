from core.polly import Polly
from core.s3 import S3Object

class Remindr(object):
    def __init__(self, phone, recording, cron):
        self.phone = phone
        self.recording = recording
        self.cron = cron

class PhoneNumber(object):
    def __init__(self, number):
        self.number = number


class Cron(object):
    def __init__(self, schedule_string):
        self.schedule_string = schedule_string


class AWSLambda(object):
    def __init__(self):
        pass

    def add_item(self, audio, phone_number, cron):
        pass
