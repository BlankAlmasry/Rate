from algorithms.rating_algorithm import RatingAlgorithmInterface
from containers.players_container import PlayersContainer
from readers.reader import Reader
from writers.writer import Writer
from util.result import Result


def compute(reader: Reader,
            writer: Writer,
            algorithm: RatingAlgorithmInterface,
            result_handler: Result):
    print("Computing...")
    players_container = PlayersContainer()
    while True:
        try:
            # read next line if exists
            player1, player2, result1 = next(reader)

            # get player ratings and decide match result according to user specification
            literal_result = result1
            p1 = find_or_create_player(algorithm, player1, players_container)
            p2 = find_or_create_player(algorithm, player2, players_container)
            try:
                result = result_handler.get_result_from_string(literal_result)
            except ValueError as error_message:
                print(error_message)
                continue

            # compute new ratings
            p1_updated, p2_updated = algorithm.compute_match(p1, p2, result)

            # update players container
            players_container.update_player(player1, p1_updated)
            players_container.update_player(player2, p2_updated)

            # write new ratings
            writer.write([
                [player1, str(p1_updated.rating)],
                [player2, str(p2_updated.rating)],
            ])
        # if no more lines to read, break, empty memory, close files and exit
        except StopIteration:
            del players_container
            reader.close()
            writer.close()
            break
    print("Done")


def fetch_file_headers(player_a_column, player_b_column, reader, result_a):
    keys = reader.keys()
    player_a_index = keys.index(player_a_column)
    player_b_index = keys.index(player_b_column)
    result_a_index = keys.index(result_a)
    return player_a_index, player_b_index, result_a_index


def find_or_create_player(algorithm, player, players_container):
    try:
        player_a_rating = players_container.get_player(player)
    except ValueError:
        player_a_rating = algorithm.rating_object()
        players_container.add_player(player, player_a_rating)
    return player_a_rating
