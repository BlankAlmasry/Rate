from algorithms.dwz.dwz_player import DWZPlayer
from algorithms.rating_algorithm import RatingAlgorithmInterface


class DWZRatingAlgorithm(RatingAlgorithmInterface):
    rating_object: DWZPlayer = DWZPlayer

    def compute_match(self, player_a: DWZPlayer, player_b: DWZPlayer, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
