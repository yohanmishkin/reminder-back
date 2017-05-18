
class Remindr(object):
    def __init__(self, phone, message, cron):
        self.phone = phone
        self.message = message
        self.cron = cron


class AzureStorage(object):
    def __init__(self):
        pass

    def savedObject(self, ocket):
        pass


class AzureFunctions(object):
    def __init__(self):
        pass

    def add_item(self, audio, phone_number, cron):
        pass

    def items(self):
        pass


class Polly(object):
    def __init__(self, location):
        pass

    def recording(self, location):
        pass