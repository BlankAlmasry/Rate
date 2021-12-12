from algorithms.ecf.ecf_player import ECFPlayer
from algorithms.rating_algorithm import RatingAlgorithmInterface


class ECFRatingAlgorithm(RatingAlgorithmInterface):
    rating_object: ECFPlayer = ECFPlayer

    def compute_match(self, player_a: ECFPlayer, player_b: ECFPlayer, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
