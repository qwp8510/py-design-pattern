from abc import ABC, abstractmethod


class Pizza(ABC):
    def __init__(self, name, dough, sauce):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = []

    def prepare(self):
        print('prepare %s' % self.name)
        print('prepare %s' % self.dough)
        print('prepare %s' % self.sauce)
        print('add topping:')
        for topping in self.toppings:
            print('topping: {}'.format(topping))

    def bake(self):
        print('bake for few minute at temperature 360')

    def cut(self):
        print('cutting the pizza')

    def box(self):
        print('place pizza into box')

    def get_name(self):
        return self.name
