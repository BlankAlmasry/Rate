class PlayerFactory:
    @staticmethod
    def create_player(algorithm_name):
        if algorithm_name == "elo":
            from players import EloPlayer
            return EloPlayer()
        elif algorithm_name == "glicko-1":
            from players import Glicko1Player
            return Glicko1Player()
        elif algorithm_name == "glicko-2":
            from players import Glicko2Player
            return Glicko2Player()
        elif algorithm_name == "trueskill":
            from players import TrueSkillPlayer
            return TrueSkillPlayer()
        elif algorithm_name == "ecf":
            from players import ECFPlayer
            return ECFPlayer()
        elif algorithm_name == "dwz":
            from players import DWZPlayer
            return DWZPlayer()
        else:
            raise ValueError("Unknown algorithm name: " + algorithm_name)
