import abc


class Writer(abc.ABC):
    @property
    @abc.abstractmethod
    def _writer(self):
        pass

    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(self.file_name, 'w+', encoding='utf-8', newline='')

    @abc.abstractmethod
    def write(self, writable):
        pass

    @abc.abstractmethod
    def write_header(self, header):
        pass

    @abc.abstractmethod
    def close(self):
        pass
