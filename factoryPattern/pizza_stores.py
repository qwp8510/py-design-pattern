from base_pizza_store import PizzaStore
from pizzas import *

class AmericaPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == 'cheese':
            return AmericaCheesePizza()
        elif item == 'veggie':
            return AmericaVeggiePizza()
        else:
            print('Your order is no longer within our service')
            return UnknownPizza()


class TaiwanPizzaStore(PizzaStore):
    def create_pizza(self, item):
        if item == 'cheese':
            return TaiwanCheesePizza()
        else:
            print('Your order is no longer within our service')
            return UnknownPizza()
