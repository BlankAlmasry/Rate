from algorithms.elo.elo_player import ELOPlayer
from algorithms.rating_algorithm import RatingAlgorithmInterface


class ELORatingAlgorithm(RatingAlgorithmInterface):
    rating_object: ELOPlayer = ELOPlayer

    def compute_match(self, player_a: ELOPlayer, player_b: ELOPlayer, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
