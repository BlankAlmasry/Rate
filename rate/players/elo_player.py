from elote import EloCompetitor

from rate.players.player import Player


class EloPlayer(Player):
    _rating_class = EloCompetitor

    def __init__(self, rating_initial=1500):
        self._rating_object = EloPlayer._rating_class(rating_initial)

    @property
    def rating(self):
        return self._rating_object.rating

    def play(self, opponent: 'EloPlayer', result):
        if result == 1:
            self._rating_object.beat(opponent._rating_object)
        elif result == 0.5:
            self._rating_object.tied(opponent._rating_object)
        elif result == 0:
            self._rating_object.lost_to(opponent._rating_object)
        return self, opponent
