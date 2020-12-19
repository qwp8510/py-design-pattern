from abc import ABC, abstractmethod


class BirdInterface(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def tweet(self):
        pass


class RedBird(BirdInterface):
    def fly(self):
        print('fly strait')

    def tweet(self):
        print('wiiiii~')

