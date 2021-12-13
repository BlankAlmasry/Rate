class ReaderFactory:
    @staticmethod
    def create_reader(extension_type, file_path, relevant_columns_indexes):
        if extension_type == "csv" or extension_type == ".csv":
            from readers.csv_reader import CsvReader
            return CsvReader(file_path, relevant_columns_indexes)
        elif extension_type == "json" or extension_type == ".json":
            from readers.json_reader import JsonReader
            return JsonReader(file_path, relevant_columns_indexes)
        else:
            raise ValueError("Unknown reader type")
