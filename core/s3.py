from boto3.s3.transfer import S3Transfer
import boto3

class S3Object(object):
    def __init__(self, bucket_name='remindrs', file=None):
        self.bucket_name = bucket_name
        self.file = file

    def location(self):
        s3 = boto3.resource('s3')
        s3.Bucket(self.bucket_name).upload_file(self.file.name, 'remindr.mp3')