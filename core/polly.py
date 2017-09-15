from boto3 import Session
from contextlib import closing
from tempfile import gettempdir
import os
import sys

class Polly(object):
    def __init__(self, message):
        self._message = message

    def recording(self, file_name):
        
        session = Session()
        polly = session.client("polly")
        
        response = polly.synthesize_speech(Text=self._message,
                                                VoiceId="Salli",
                                                OutputFormat="mp3")

        if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join(gettempdir(), file_name)
                try:
                    # Open a file for writing the output as a binary stream
                    with open(output, "wb") as file:
                        file.write(stream.read())
                        return output

                except IOError as error:
                    # Could not write to file, exit gracefully
                    print(error)
                    sys.exit(-1)