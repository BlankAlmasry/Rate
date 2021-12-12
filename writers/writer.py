import abc


class Writer(abc.ABC):
    @property
    @abc.abstractmethod
    def _writer(self):
        pass

    def __init__(self, file_name, keys):
        self.file_name = file_name
        self.file = open(self.file_name, 'w+', encoding='utf-8', newline='')
        self.keys = keys

    @abc.abstractmethod
    def write(self, writable):
        pass

    @property
    @abc.abstractmethod
    def keys(self):
        pass

    @keys.setter
    def keys(self, keys):
        pass

    @abc.abstractmethod
    def close(self):
        pass
