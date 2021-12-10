import csv

from readers.reader import Reader


class CsvReader(Reader):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.reader = csv.reader(self.file)
        self._keys = next(self.reader)

    def __next__(self):
        return next(self.reader)

    def __iter__(self):
        return self.reader

    def keys(self):
        return self._keys
