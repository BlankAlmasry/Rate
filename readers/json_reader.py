from readers.reader import Reader


class JsonReader(Reader):
    def __init__(self, file_name):
        super().__init__(file_name)

    def __next__(self):
        pass

    def __iter__(self):
        pass

    def keys(self) -> list:
        pass

    def close(self):
        pass
