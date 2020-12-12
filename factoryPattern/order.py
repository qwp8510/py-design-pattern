from pizza_stores import *


def main():
    america_store = TaiwanPizzaStore()
    pizza = america_store.order_pizza('cheese')
    print('Welcome to Ameriza pizza store, your order is {}'.format(pizza.get_name()))


if __name__ == '__main__':
    main()