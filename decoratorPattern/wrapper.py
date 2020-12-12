from abc import abstractmethod

from base import Beverage


class Condiment(Beverage):
    @abstractmethod
    def get_description(self):
        pass


class Mocha(Condiment):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Mocha'

    def cost(self):
        return self.beverage.cost() + 15


class Whip(Condiment):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Whip'

    def cost(self):
        return self.beverage.cost() + 10


class Milk(Condiment):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ', Milk'

    def cost(self):
        return self.beverage.cost() + 30
