from base import Beverage


class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 160


class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'DarkRoast'

    def cost(self):
        return 180
