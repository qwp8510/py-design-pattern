from drink import Coco, Coffee


class DrinkMachine():
    DRINK = {'coco': Coco, 'coffee': Coffee}

    def __init__(self, drink_type):
        self.drink = self.DRINK.get(drink_type)()

    def press_prepare_button(self):
        self.drink.prepare()


def main():
    DrinkMachine('coco').press_prepare_button()
    DrinkMachine('coffee').press_prepare_button()


if __name__ == '__main__':
    main()
