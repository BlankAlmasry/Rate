supported_readers = {
    'csv': {
        'path': 'readers.csv_reader',
        'class': 'CsvReader'
    },
    'json': {
        'path': 'readers.json_reader',
        'class': 'JsonReader'
    }
}
supported_writers = {
    'csv': {
        'path': 'writers.csv_writer',
        'class': 'CsvWriter'
    },
    'json': {
        'path': 'writers.json_writer',
        'class': 'JsonWriter'
    }
}
supported_algorithms = {
    'elo': {
        'path': 'algorithms.elo.elo_rating_algorithm',
        'class': 'ELORatingAlgorithm'
    },
}
