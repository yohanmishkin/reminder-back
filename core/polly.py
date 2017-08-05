from boto3 import Session
from contextlib import closing
from tempfile import gettempdir
import os
import sys

class Polly(object):
    def __init__(self, message):
        self.message = message

    def recording(self):
        
        session = Session()
        polly = session.client("polly", region_name='us-east-1')
        
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