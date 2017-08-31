from boto3 import Session
import botocore

class S3Object(object):
    def __init__(self, bucket_name='remindrs', file=None):
        self._bucket_name = bucket_name
        self._file = file

    def location(self):
        session = Session()
        s3 = session.client("s3")
        s3.upload_file(self._file.name, self._bucket_name, self._file.name)

        url = 'https://s3.us-east-2.amazonaws.com/{0}/{1}'.format(self._bucket_name,
                                                                  self._file.name)
        return url