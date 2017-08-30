from boto3 import Session
import botocore

class S3Object(object):
    def __init__(self, bucket_name='remindrs', file=None):
        self.bucket_name = bucket_name
        self.file = file

    def location(self):
        session = Session()
        s3 = session.client("s3")
        s3.upload_file(self.file.name, self.bucket_name, self.file.name)
        
        url = 'https://s3.us-east-2.amazonaws.com/{0}/{1}'.format(self.bucket_name, 
                                                                  self.file.name)
        return url