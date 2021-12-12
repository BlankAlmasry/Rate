from algorithms.glicko1.glicko1_player import Glicko1Player
from algorithms.rating_algorithm import RatingAlgorithmInterface


class Glicko1RatingAlgorithm(RatingAlgorithmInterface):
    rating_object: Glicko1Player = Glicko1Player

    def compute_match(self, player_a: Glicko1Player, player_b: Glicko1Player, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
