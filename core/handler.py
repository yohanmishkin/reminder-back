STORAGE = 's3'
AUDIO_GENERATOR = 'polly'
PHONE_OPERATOR = 'twilio'


class Handler(object):
    def __init__(self, audio, storage, scheduler):
        self.audio = audio
        self.storage = storage
        self.schedule = scheduler

    def run(self, event):
        audio = self.audio.recording(event["message"])
        saved_audio = self.storage.save(audio)
        self.schedule.add_item(saved_audio, event['phone'], event['cron'])