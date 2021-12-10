import abc
from typing import Type

from algorithms.player import Player


class RatingAlgorithmInterface(abc.ABC):
    @property
    @abc.abstractmethod
    def rating_object(self) -> Type[Player]:
        return Player

    def compute_match(self, player_a: Player, player_b: Player, result_a) -> Player:
        pass
