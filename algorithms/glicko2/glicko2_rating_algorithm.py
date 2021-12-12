from algorithms.glicko2.glicko2_player import Glicko2Player
from algorithms.rating_algorithm import RatingAlgorithmInterface


class Glicko2RatingAlgorithm(RatingAlgorithmInterface):
    rating_object: Glicko2Player = Glicko2Player

    def compute_match(self, player_a: Glicko2Player, player_b: Glicko2Player, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
