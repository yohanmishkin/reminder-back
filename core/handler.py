STORAGE = 's3'
AUDIO_GENERATOR = 'polly'
PHONE_OPERATOR = 'twilio'

class RemindrFunction:
    def __init__(self, audio, storage, scheduler):
        self.audio = audio
        self.storage = storage
        self.scheduler = scheduler

    def run(self, event):
        audio = self.audio.recording(event["message"])
        saved_audio = self.storage.savedObject(audio)
        self.scheduler.schedule(saved_audio, event['phone'], event['cron'])