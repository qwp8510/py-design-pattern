from components.chefs import HappyBreakfastShopChef
from components.waiters import HappyBreakfastShopWaiter
from components.cashier import HappyBreakfastShopCashier


class HappyBreakfastShop():
    def __init__(self, character):
        self.character = character
        self.chef = HappyBreakfastShopChef()
        self.waiter = HappyBreakfastShopWaiter()
        self.cashier = HappyBreakfastShopCashier()

    def order(self, meal):
        self.waiter.order(meal)

    def prepare(self, meal):
        self.chef.prepare(meal)

    def cook(self, meal):
        self.chef.cook(meal)

    def serve(self, meal):
        self.waiter.serve(meal)

    def check(self, meal):
        self.cashier.check(meal)

    def clean(self):
        self.waiter.clean()

    def eat(self, meal):
        self.order(meal)
        self.prepare(meal)
        self.cook(meal)
        self.serve(meal)
        self.character.eat(meal)
        self.check(meal)
        self.clean()
