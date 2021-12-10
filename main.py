import os

from algorithms.elo.ELOPlayer import ELOPlayer
from algorithms.rating_algorithm import RatingAlgorithmInterface
from containers.players_container import PlayersContainer
from readers.csv_reader import CsvReader
from readers.json_reader import JsonReader
from readers.reader import Reader
from writers.csv_writer import CsvWriter
from writers.writer import Writer


def compute(reader: Reader,
            writer: Writer,
            player_a,
            player_b,
            result_a,
            algorithm: RatingAlgorithmInterface,
            result_win,
            result_loss,
            result_draw):
    print("Computing...")
    keys = reader.keys()
    player_a_index = keys.index(player_a)
    player_b_index = keys.index(player_b)
    result_a_index = keys.index(result_a)
    players_container = PlayersContainer()
    while True:
        try:
            match_record = next(reader)
            try:
                player_a_rating = players_container.get_player(match_record[player_a_index])
            except ValueError:
                player_a_rating = algorithm.rating_object()
                players_container.add_player(match_record[player_a_index], player_a_rating)
            try:
                player_b_rating = players_container.get_player(match_record[player_b_index])
            except ValueError:
                player_b_rating = algorithm.rating_object()
                players_container.add_player(match_record[player_b_index], player_b_rating)

            if match_record[result_a_index].casefold() == result_win.casefold():
                result = 1
            elif match_record[result_a_index].casefold() == result_loss.casefold():
                result = 0
            elif match_record[result_a_index].casefold() == result_draw.casefold():
                result = 0.5
            else:
                print(f"unsupported result on line // TODO")
                continue
            print(result)
            player_a_new_rating, player_b_new_rating = algorithm.compute_match(player_a_rating,
                                                                               player_b_rating,
                                                                               result)
            players_container.update_player(match_record[player_a_index], player_a_new_rating)
            players_container.update_player(match_record[player_b_index], player_b_new_rating)
            writer.write([
                [match_record[player_a_index], str(player_a_new_rating.rating.rating)],
                [match_record[player_b_index], str(player_b_new_rating.rating.rating)],
            ])
        except StopIteration:
            print(len(players_container.players))
            del players_container
            break
    print("Done")


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

    compute(reader, writer, player_a, player_b, result_a,
            algorithm,
            result_win, result_loss, result_draw,
            )


if __name__ == "__main__":
    main('fights.csv', 'fighter1', 'fighter2', 'result1',
         'elo', 'csv',
         result_win='win',
         result_loss='loss',
         result_draw='draw')
