import pathlib


class FileName(object):
    def __init__(self, file_name):
        self._file_name = file_name

    def stem(self):
        return pathlib.Path(self._file_name).stem

    def full(self):
        return self._file_name
