class WriterFactory:
    @staticmethod
    def create_writer(output_file_name, headers):
        if output_file_name.endswith('.csv'):
            from writers.csv_writer import CsvWriter
            return CsvWriter(output_file_name, headers)
        elif output_file_name.endswith('.json'):
            from writers.json_writer import JsonWriter
            return JsonWriter(output_file_name, headers)
