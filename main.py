from __future__ import print_function, unicode_literals

import json
import os

from calculator.calculator import Calculator
from gui.gui import GUI
from readers.reader_factory import ReaderFactory
from utils.result_handler import ResultHandler


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win, result_loss, result_draw,
         algorithms, readers, writers):
    # chose all algorithms
    if algorithm_name == "all":
        # recursively call main with all algorithms
        for algo in algorithms:
            main(file, player_a_index, player_b_index, result_a_index,
                 algo, output_format,
                 result_win, result_loss, result_draw,
                 algorithms, readers, writers)
        return

    name, extension = os.path.splitext(file)

    # create reader
    columns_indexes = [player_a_index, player_b_index, result_a_index]
    reader = ReaderFactory.create_reader(extension, file, columns_indexes)

    # create writer
    if output_format in writers:
        w = writers[output_format]
        exec(f"from {w['path']} import {w['class']}")
        writer = eval(w["class"])(name + "_" + algorithm_name + "." + output_format, keys=["name", "rating"])
    else:
        print("Output format not supported")
        return

    # create result handler to handle results according to the user specifications
    result_handler = ResultHandler(result_win, result_loss, result_draw)

    # start calculation
    calculator = Calculator(reader, writer, algorithm_name, result_handler)
    calculator.calculate()
    del calculator


if __name__ == "__main__":
    # example answers
    answers = {
        'file': 'fights.json',
        'player_a_index': '0',
        'player_b_index': '1',
        'result_a_index': '2',
        'algorithm_name': 'all',
        'output_format': 'json',
        'result_win': 'Win',
        'result_loss': 'loss',
        'result_draw': 'Draw',
    }

    with open('config.json', 'r') as config:
        config = json.load(config)
        supported_algorithms = config["supported_algorithms"]
        supported_readers = config["supported_readers"]
        supported_writers = config["supported_writers"]

    # answers = GUI.display(supported_readers, supported_writers, supported_algorithms)
    print("Computing...")
    main(algorithms=supported_algorithms, readers=supported_readers, writers=supported_writers, **answers)
    print("Done")
