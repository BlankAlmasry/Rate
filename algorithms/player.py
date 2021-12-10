import abc


class PlayerInterface(abc.ABC):
    @abc.abstractmethod
    def rating(self) -> int:
        pass

    @abc.abstractmethod
    def play(self, opponent: 'PlayerInterface', result):
        pass
