import boto3

class S3Object(object):
    def __init__(self, bucket_name, file_name, key):
        self._bucket_name = bucket_name
        self._file_name = file_name
        self._key = key

    def url(self):
        s3 = boto3.client("s3")
        s3.upload_file(self._file_name, self._bucket_name, self._key)

        url = 'https://s3.us-east-1.amazonaws.com/{0}/{1}'.format(self._bucket_name, self._key)

        return url

    def delete(self):
        s3 = boto3.client("s3")
        s3.delete_object(Bucket=self._bucket_name, Key=self._key)