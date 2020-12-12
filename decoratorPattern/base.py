from abc import ABC


class Beverage(ABC):
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description
