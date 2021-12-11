from __future__ import print_function, unicode_literals
import os

from config import supported_readers, supported_algorithms, supported_writers
from calculator.calculator import Calculator
from util.result import ResultHandler


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win="1", result_loss="0", result_draw="0.5"):
    name, extension = os.path.splitext(file)

    # create reader
    columns_indexes = [player_a_index, player_b_index, result_a_index]
    if extension[1:] in supported_readers:
        r = supported_readers[extension[1:]]
        exec(f"from {r['path']} import {r['class']}")
        reader = eval(r["class"])(file, columns_indexes)
    else:
        print("Unsupported file format")
        return
    # Choose algorithm
    if algorithm_name in supported_algorithms:
        a = supported_algorithms[algorithm_name]
        exec(f"from {a['path']} import {a['class']}")
        algorithm = eval(a["class"])()
    else:
        print("Algorithm not supported")
        return

    # create writer
    if output_format in supported_writers:
        w = supported_writers[output_format]
        exec(f"from {w['path']} import {w['class']}")
        writer = eval(w["class"])(name + "_" + algorithm_name + "." + output_format)
    else:
        print("Output format not supported")
        return

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
