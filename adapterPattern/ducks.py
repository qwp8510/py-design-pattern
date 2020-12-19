from abc import ABC, abstractmethod


class DuckInterface(ABC):
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def quack(self):
        pass


class Mallard(DuckInterface):
    def fly(self):
        print('fly strait')

    def quack(self):
        print('quack! quack!')
