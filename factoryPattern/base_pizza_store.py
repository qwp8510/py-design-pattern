from abc import ABC, abstractmethod


class PizzaStore(ABC):
    def order_pizza(self, item):
        pizza = self.create_pizza(item)
        print()
        if pizza.__class__.__name__ == 'UnknownPizza':
            return pizza
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, item):
        pass
