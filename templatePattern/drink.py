from drink_vending_machine import HotCocoVendingMachine


class Coco(HotCocoVendingMachine):
    def add_powder(self):
        print('add coco powder')

    def add_condiments(self):
        print('add nothing')


class Coffee(HotCocoVendingMachine):
    def add_powder(self):
        print('add coffee powder')

    def add_condiments(self):
        print('add suger')

    def want_condiments(self):
        answer = input('do you want sugar?')
        if answer == 'n' or answer == 'N':
            return False
        else:
            return True
