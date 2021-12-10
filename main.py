import os

from calculator import compute
from readers.csv_reader import CsvReader
from readers.json_reader import JsonReader
from writers.csv_writer import CsvWriter


def main(file, player_a, player_b, result_a,
         algorithm_name, output_format,
         result_win="1", result_loss="0", result_draw="0.5"):
    print("Hello World")
    name, extension = os.path.splitext(file)
    if extension == ".csv":
        reader = CsvReader(file)
    elif extension == ".json":
        reader = JsonReader(file)
    else:
        print("unsupported file format")
        return
    if algorithm_name == 'elo':
        from algorithms.elo.elo_rating_algorithm import ELORatingAlgorithm
        algorithm = ELORatingAlgorithm()
    else:
        algorithm = None
    writer = CsvWriter(name + "_" + algorithm_name + "." + output_format)

    compute(reader, writer, player_a, player_b, result_a, algorithm, result_win, result_loss, result_draw)


if __name__ == "__main__":
    main('fights.csv', 'fighter1', 'fighter2', 'result1',
         'elo', 'csv',
         result_win='win',
         result_loss='loss',
         result_draw='draw')
