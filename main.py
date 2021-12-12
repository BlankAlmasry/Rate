from __future__ import print_function, unicode_literals

import json
import os

from calculator.calculator import Calculator
from gui.gui import GUI
from utils.result_handler import ResultHandler


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win, result_loss, result_draw,
         algorithms, readers, writers):
    name, extension = os.path.splitext(file)

    # create reader
    columns_indexes = [player_a_index, player_b_index, result_a_index]
    if extension[1:] in readers:
        r = readers[extension[1:]]
        exec(f"from {r['path']} import {r['class']}")
        reader = eval(r["class"])(file, columns_indexes)
    else:
        print("Unsupported file format")
        return

    # chose all algorithms
    if algorithm_name == "all":
        # recursively call main with all algorithms
        for algorithm in algorithms:
            main(file, player_a_index, player_b_index, result_a_index,
                 algorithm, output_format,
                 result_win, result_loss, result_draw,
                 algorithms, readers, writers)
        return
    # Choose a single algorithm
    elif algorithm_name in algorithms:
        a = algorithms[algorithm_name]
        exec(f"from {a['path']} import {a['class']}")
        algorithm = eval(a["class"])()
    else:
        print("Algorithm not supported")
        return

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
    calculator = Calculator(reader, writer, algorithm, result_handler)
    calculator.calculate()
    del calculator


if __name__ == "__main__":
    # example answers
    # answers = {
    #     'file': 'fights.csv',
    #     'player_a_index': '0',
    #     'player_b_index': '1',
    #     'result_a_index': '2',
    #     'algorithm_name': 'all',
    #     'output_format': 'json',
    #     'result_win': 'Win',
    #     'result_loss': 'loss',
    #     'result_draw': 'Draw',
    # }

    with open('config.json', 'r') as config:
        config = json.load(config)
        supported_algorithms = config["supported_algorithms"]
        supported_readers = config["supported_readers"]
        supported_writers = config["supported_writers"]

    answers = GUI.display(supported_readers, supported_writers, supported_algorithms)
    print("Computing...")
    main(algorithms=supported_algorithms, readers=supported_readers, writers=supported_writers, **answers)
    print("Done")
