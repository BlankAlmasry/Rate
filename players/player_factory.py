class PlayerFactory:
    @staticmethod
    def create_player(algorithm_name):
        if algorithm_name == "elo":
            from players.elo_player import EloPlayer
            return EloPlayer()
        elif algorithm_name == "glicko-1":
            from players.glicko1_player import Glicko1Player
            return Glicko1Player()
        elif algorithm_name == "glicko-2":
            from players.glicko2_player import Glicko2Player
            return Glicko2Player()
        elif algorithm_name == "trueskill":
            from players.trueskill_player import TrueSkillPlayer
            return TrueSkillPlayer()
        elif algorithm_name == "ecf":
            from players.ecf_player import ECFPlayer
            return ECFPlayer()
        elif algorithm_name == "dwz":
            from players.dwz_player import DWZPlayer
            return DWZPlayer()
        else:
            raise ValueError("Unknown algorithm name: " + algorithm_name)
