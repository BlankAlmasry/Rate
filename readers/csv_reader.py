import csv

from readers.reader import Reader


class CsvReader(Reader):
    def __init__(self, file_name, columns: list = None):
        super().__init__(file_name, columns)
        self._reader = csv.reader(self.file)
        self._keys = next(self._reader)

    def __next__(self):
        return next(self._reader)

    def __iter__(self):
        return self._reader

    def keys(self):
        return self._keys
