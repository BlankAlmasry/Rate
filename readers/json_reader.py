from readers.reader import Reader


class JsonReader(Reader):
    def __init__(self, file_name, columns_indexes: list):
        super().__init__(file_name, columns_indexes)

    def next_record(self):
        pass

    def __next__(self):
        pass

    def __iter__(self):
        pass

    def keys(self) -> list:
        pass

    def close(self):
        pass
