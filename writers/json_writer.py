from writers.writer import Writer


class JsonWriter(Writer):
    def __init__(self, file_name):
        super().__init__(file_name)

    def write(self, data):
        pass