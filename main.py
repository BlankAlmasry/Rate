from __future__ import print_function, unicode_literals
import os
from PyInquirer import prompt

from calculator.calculator import Calculator
from readers.csv_reader import CsvReader
from readers.json_reader import JsonReader
from util.result import ResultHandler
from writers.csv_writer import CsvWriter


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win="1", result_loss="0", result_draw="0.5"):
    name, extension = os.path.splitext(file)
    # create reader
    columns_indexes = [player_a_index, player_b_index, result_a_index]
    if extension == ".csv":
        reader = CsvReader(file, columns_indexes=columns_indexes)
    elif extension == ".json":
        reader = JsonReader(file, columns_indexes=columns_indexes)
    else:
        print("unsupported file format")
        return
    # Choose algorithm
    if algorithm_name == 'elo':
        from algorithms.elo.elo_rating_algorithm import ELORatingAlgorithm
        algorithm = ELORatingAlgorithm()
    else:
        algorithm = None

    # create writer
    writer = CsvWriter(name + "_" + algorithm_name + "." + output_format)

    # create result handler to handle results according to the user specifications
    result_handler = ResultHandler(result_win, result_loss, result_draw)

    # start calculation
    calculator = Calculator(reader, writer, algorithm, result_handler)
    print("Computing...")
    calculator.calculate()
    print("Done!")
if __name__ == "__main__":
    questions = [
        {
            'type': 'input',
            'name': 'file',
            'message': 'Path to file with matches (csv or json):',
        },
        {
            'type': 'input',
            'name': 'player_a_index',
            'message': 'First Player Key: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'input',
            'name': 'player_b_index',
            'message': 'Second Player Key: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'input',
            'name': 'result_a_index',
            'message': 'Result for player A: (assuming first column is 0, second 1, etc.)',
        },
        {
            'type': 'list',
            'name': 'algorithm_name',
            'message': 'Algorithm you want to use to rate the matches:',
            'choices': ['elo', 'glicko-2'],
        },
        {
            'type': 'list',
            'name': 'output_format',
            'message': 'Output format:',
            'choices': ['csv', 'json'],
        },
        {
            'type': 'input',
            'name': 'result_win',
            'message': 'Result for a win:(how would a win is typed in the result column)',
        },
        {
            'type': 'input',
            'name': 'result_loss',
            'message': 'Result for a loss:(how would a loss is typed in the result column)',
        },
        {
            'type': 'input',
            'name': 'result_draw',
            'message': 'Result for a draw:(how would a win is typed in the result column)',
        },
    ]
    # example answers
    answers = {
        'file': 'fights.csv',
        'player_a_index': '0',
        'player_b_index': '1',
        'result_a_index': '2',
        'algorithm_name': 'elo',
        'output_format': 'csv',
        'result_win': 'Win',
        'result_loss': 'loss',
        'result_draw': 'Draw',

    }
    # answers = prompt(questions)
    main(**answers)
    print("Done")
