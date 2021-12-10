from elote import EloCompetitor

from algorithms.player import PlayerInterface


class ELOPlayer(PlayerInterface):
    def __init__(self, rating_initial=1500):
        self.rating = EloCompetitor(rating_initial)

    def rating(self):
        return self.rating

    def play(self, opponent: 'ELOPlayer', result):
        print(f'{self.rating.rating} vs {opponent.rating.rating}')
        print(f'result {result}')
        if result == 1:
            self.rating.beat(opponent.rating)
        elif result == 0.5:
            self.rating.tied(opponent.rating)
        elif result == 0:
            self.rating.lost_to(opponent.rating)
        print(f'{self.rating.rating} vs {opponent.rating.rating}')
        return self, opponent
