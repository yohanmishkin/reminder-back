import boto3

from core.utilities.filename import FileName


class S3Object(object):
    def __init__(self, bucket_name, folder_name, file_name):
        self._bucket_name = bucket_name
        self._folder_name = folder_name
        self._file_name = FileName(file_name)

    def url(self):
        s3 = boto3.client("s3")

        s3.upload_file(
            self._file_name.full(),
            self._bucket_name,
            '{0}{1}'.format(self._folder_name, self._file_name.full())
        )

        return 'https://s3.us-east-1.amazonaws.com/{0}/{1}{2}'.format(
            self._bucket_name,
            self._folder_name,
            self._file_name.full()
        )

    def delete(self):
        s3 = boto3.client("s3")

        s3.delete_object(
            Bucket=self._bucket_name,
            Key='{0}/{1}'.format(self._folder_name, self._file_name.full())
        )
