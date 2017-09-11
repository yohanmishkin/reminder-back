import boto3
import uuid

class S3Object(object):
    def __init__(self, bucket_name='remindrs', file_name=None):
        self._bucket_name = bucket_name
        self._file_name = file_name

    def url(self):
        s3 = boto3.client("s3")
        key = str(uuid.uuid4())

        s3.upload_file(self._file_name, self._bucket_name, key)

        url = 'https://s3.us-east-1.amazonaws.com/{0}/{1}'.format(self._bucket_name, key)
        return url