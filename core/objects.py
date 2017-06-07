from boto3 import Session
from contextlib import closing
from tempfile import gettempdir
import os
import sys

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


class S3Object(object):
    def __init__(self):
        pass

    def savedObject(self, ocket):
        pass


class AWSLambda(object):
    def __init__(self):
        pass

    def add_item(self, audio, phone_number, cron):
        pass


class Polly(object):
    def __init__(self, message):
        self.message = message

    def recording(self):
        
        session = Session()
        polly = session.client("polly")
        
        try: 
            response = polly.synthesize_speech(Text=self.message,
                                                   VoiceId="Salli",
                                                   OutputFormat="mp3")

            if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                    output = os.path.join(gettempdir(), "remindr.mp3")
                    try:
                        # Open a file for writing the output as a binary stream
                        with open(output, "wb") as file:
                            file.write(stream.read())
                            return output

                    except IOError as error:
                        # Could not write to file, exit gracefully
                        print(error)
                        sys.exit(-1)
        except:
            # The service returned an error, exit gracefully
            raise