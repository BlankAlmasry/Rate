from __future__ import print_function, unicode_literals
import os
from PyInquirer import prompt

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
    questions = [
        {
            'type': 'input',
            'name': 'file',
            'message': 'Path to file with matches (csv or json):',
        },
        {
            'type': 'input',
            'name': 'player_a',
            'message': 'First Player Key: (column header or key, pick a unique identifier for each player)',
        },
        {
            'type': 'input',
            'name': 'player_b',
            'message': 'Second Player Key: (column header or key, pick a unique identifier for each player)',
        },
        {
            'type': 'input',
            'name': 'result_a',
            'message': 'Result for player A: (column header or key)',
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

    answers = prompt(questions)
    print(answers)
    main(answers['file'], answers['player_a'], answers['player_b'], answers['result_a'], answers['algorithm_name'],
         answers['output_format'], answers['result_win'], answers['result_loss'], answers['result_draw'])

# TODO: add support for glicko-2
# TODO: support for json
# TODO: actually use the GUI
# TODO: actually use output format
# TODO: refactor calculator file, it's disturbing
# TODO: perhaps seperate GUI and main file
