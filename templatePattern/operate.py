from drink import Coco, Coffee


class DrinkMachine():
    DRINK = {'coco': Coco, 'coffee': Coffee}

    def __init__(self):
        self._drink = None

    def order(self, drink_type):
        self._drink = self.DRINK.get(drink_type)()

    def press_prepare_button(self):
        self._drink.prepare()


def main():
    drink_machine = DrinkMachine()
    drink_machine.order('coco')
    drink_machine.press_prepare_button()
    drink_machine.order('coffee')
    drink_machine.press_prepare_button()


if __name__ == '__main__':
    main()
