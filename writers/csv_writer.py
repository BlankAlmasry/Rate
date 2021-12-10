import csv

from writers.writer import Writer


class CsvWriter(Writer):
    _writer = None

    def __init__(self, file_name):
        super().__init__(file_name)
        self._writer = csv.writer(self.file)

    def write(self, data: list):
        for row in data:
            self._writer.writerow(row)

    def write_header(self, header: list):
        self._writer.writerow(','.join(header) + '\n')

    def close(self):
        self.file.close()
