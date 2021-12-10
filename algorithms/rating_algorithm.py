import abc
from typing import Type

from algorithms.player import PlayerInterface


class RatingAlgorithmInterface(abc.ABC):
    @property
    @abc.abstractmethod
    def rating_object(self) -> Type[PlayerInterface]:
        return PlayerInterface

    def compute_match(self, player_a: PlayerInterface, player_b: PlayerInterface, result_a) -> PlayerInterface:
        pass
