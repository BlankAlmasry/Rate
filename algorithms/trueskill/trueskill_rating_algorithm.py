from algorithms.rating_algorithm import RatingAlgorithmInterface
from algorithms.trueskill.trueskill_player import TrueSkillPlayer


class TrueSkillRatingAlgorithm(RatingAlgorithmInterface):
    rating_object: TrueSkillPlayer = TrueSkillPlayer

    def compute_match(self, player_a: TrueSkillPlayer, player_b: TrueSkillPlayer, score_a):
        player_a, player_b = player_a.play(player_b, score_a)

        return player_a, player_b
