from abc import ABC, abstractmethod


class FlyInterface(ABC):
    @abstractmethod
    def fly(self):
        pass


class StraightFly(FlyInterface):
    def fly(self):
        print('fly strait')


class FastFly(FlyInterface):
    def fly(self):
        print('fly fast')


class FlyNoWay(FlyInterface):
    def fly(self):
        print('can not fly')
