from algorithms.rating_algorithm import RatingAlgorithmInterface
from containers.players_container import PlayersContainer
from readers.reader import Reader
from writers.writer import Writer
from util.result import ResultHandler


def compute(reader: Reader,
            writer: Writer,
            algorithm: RatingAlgorithmInterface,
            result_handler: ResultHandler):
    print("Computing...")
    players_container = PlayersContainer()
    while True:
        try:
            # read next line if exists
            player1, player2, result_for_player1 = reader.next_record()

            # get player ratings and decide match result according to user specification
            p1, p2 = players_container.find_or_add_players([
                [player1, algorithm.rating_object()],
                [player2, algorithm.rating_object()]
            ])

            # get result in terms of 1, 0 or 0.5, if text is not recognized, skip it
            try:
                result = result_handler.get_result_from_string(result_for_player1)
            except ValueError as error_message:
                print(error_message)
                continue

            # compute new ratings
            p1_updated, p2_updated = algorithm.compute_match(p1, p2, result)

            # update players container
            players_container.update_players([[player1, p1_updated], [player2, p2_updated]])

            # write new ratings
            writer.write([
                [player1, str(p1_updated.rating)],
                [player2, str(p2_updated.rating)],
            ])
        # if no more lines to read, break, empty the memory, close the files and exit
        except StopIteration:
            del players_container
            reader.close()
            writer.close()
            break
    print("Done")
