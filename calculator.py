from algorithms.rating_algorithm import RatingAlgorithmInterface
from containers.players_container import PlayersContainer
from readers.reader import Reader
from writers.writer import Writer


def compute(reader: Reader,
            writer: Writer,
            player_a_column,
            player_b_column,
            result_a,
            algorithm: RatingAlgorithmInterface,
            result_win,
            result_loss,
            result_draw):
    print("Computing...")

    player_a_index, player_b_index, result_a_index = fetch_file_headers(player_a_column, player_b_column, reader,
                                                                        result_a)
    players_container = PlayersContainer()
    while True:
        try:
            # read next line if exists
            match_record = next(reader)

            # get player ratings and decide match result according to user specification
            literal_result = match_record[result_a_index]
            p1 = find_or_create_player(algorithm, match_record, player_a_index, players_container)
            p1_name = match_record[player_a_index]
            p2 = find_or_create_player(algorithm, match_record, player_b_index, players_container)
            p2_name = match_record[player_b_index]
            try:
                result = decide_match_result_according_to_user_specification(literal_result,
                                                                             result_win,
                                                                             result_loss,
                                                                             result_draw)
            except ValueError as error_message:
                print(error_message)
                continue

            # compute new ratings
            p1_updated, p2_updated = algorithm.compute_match(p1, p2, result)

            # update players container
            players_container.update_player(p1_name, p1_updated)
            players_container.update_player(p2_name, p2_updated)

            # write new ratings
            writer.write([
                [p1_name, str(p1_updated.rating)],
                [p2_name, str(p2_updated.rating)],
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


def find_or_create_player(algorithm, match_record, player_a_index, players_container):
    try:
        player_a_rating = players_container.get_player(match_record[player_a_index])
    except ValueError:
        player_a_rating = algorithm.rating_object()
        players_container.add_player(match_record[player_a_index], player_a_rating)
    return player_a_rating


def decide_match_result_according_to_user_specification(result, result_win, result_loss, result_draw):
    if result.casefold() == result_win.casefold():
        return 1
    elif result.casefold() == result_loss.casefold():
        return 0
    elif result.casefold() == result_draw.casefold():
        return 0.5
    else:
        raise ValueError(f"unsupported result [{result}], expected [{result_win}], [{result_loss}] or [{result_draw}]")
