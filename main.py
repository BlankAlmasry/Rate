from __future__ import print_function, unicode_literals

import json
import os

from calculator.calculator import Calculator
from gui.gui import GUI
from util.result_handler import ResultHandler


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win="1", result_loss="0", result_draw="0.5"):
    name, extension = os.path.splitext(file)

    # fetch config
    with open('config.json', 'r') as config:
        config = json.load(config)
        supported_algorithms = config["supported_algorithms"]
        supported_readers = config["supported_readers"]
        supported_writers = config["supported_writers"]

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
    #     'file': 'fights.json',
    #     'player_a_index': '0',
    #     'player_b_index': '1',
    #     'result_a_index': '2',
    #     'algorithm_name': 'elo',
    #     'output_format': 'csv',
    #     'result_win': 'Win',
    #     'result_loss': 'loss',
    #     'result_draw': 'Draw',
    # }

    answers = GUI.display()
    print("Computing...")
    main(**answers)
    print("Done")
