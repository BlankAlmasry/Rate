from __future__ import print_function, unicode_literals

import json
import os

from calculator.calculator import Calculator
from gui.gui import GUI
from readers.reader_factory import ReaderFactory
from utils.result_handler import ResultHandler
from writers.writer_factory import WriterFactory


def main(file, player_a_index, player_b_index, result_a_index,
         algorithm_name, output_format,
         result_win, result_loss, result_draw):
    name, extension = os.path.splitext(file)

    # create reader
    columns_indexes = [player_a_index, player_b_index, result_a_index]
    reader = ReaderFactory.create_reader(extension, file, columns_indexes)

    # create writer
    output_file_name = name + "_" + algorithm_name + "." + output_format
    writer = WriterFactory.create_writer(output_file_name, headers=["name", "rating"])

    # create result handler to handle results according to the user specifications
    result_handler = ResultHandler(result_win, result_loss, result_draw)

    # start calculation
    calculator = Calculator(reader,
                            writer,
                            algorithm_name if algorithm_name != 'all' else supported_algorithms,
                            result_handler)
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
        'output_format': 'csv',
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
    if answers['algorithm_name'] == 'all':
        for algorithm in supported_algorithms:
            print(f"Computing {answers['algorithm_name']} ratings...")
            answers["algorithm_name"] = algorithm
            main(**answers)
    else:
        print(f"Computing {answers['algorithm_name']} ratings...")
        main(**answers)
    print("Done")
