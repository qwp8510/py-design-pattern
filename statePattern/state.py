from abc import ABC, abstractmethod


class StateInterface(ABC):
    @abstractmethod
    def insert_money(self):
        pass

    @abstractmethod
    def eject_money(self):
        pass

    @abstractmethod
    def press_button(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class SoldState(StateInterface):
    def __init__(self, vending_maching):
        self.vending_maching = vending_maching

    def insert_money(self, money=0):
        print('You can not insert money on sold state and we ready to dispense your coffee')

    def eject_money(self):
        print('Sorry, You already press  button and we ready to dispense your coffee')

    def press_button(self):
        print('Wait! You already press  button. Do not press twice')

    def dispense(self):
        self.vending_maching.release()
        if self.vending_maching.get_num() <= 0:
            self.vending_maching.set_state(self.vending_maching.get_sold_out_state())
        else:
            self.vending_maching.set_state(self.vending_maching.get_no_money_state())


class SoldOutState(StateInterface):
    def __init__(self, vending_maching):
        self.vending_maching = vending_maching

    def insert_money(self, money=0):
        print('You can not insert money, because the machine is sold out')

    def eject_money(self):
        print('You can not eject money, because you have not insert money')

    def press_button(self):
        print('You can not press button, because the machine is sold out')

    def dispense(self):
        print('Nothing dispensed, because the machine is sold out')


class NoMoneyState(StateInterface):
    def __init__(self, vending_maching):
        self.vending_maching = vending_maching

    def insert_money(self, money=0):
        print('You insert money: {}'.format(money))
        self.vending_maching.set_state(self.vending_maching.get_has_money_state())

    def eject_money(self):
        print('You have not insert a money')

    def press_button(self):
        print('Nothing happened, because you have not insert a money')

    def dispense(self):
        print('You need to pay first')


class HasMoneyState(StateInterface):
    def __init__(self, vending_maching):
        self.vending_maching = vending_maching

    def insert_money(self, money=0):
        print('You can not insert money, because you already insert')

    def eject_money(self):
        print('money returned')
        self.vending_maching.set_state(self.vending_maching.get_no_money_state())

    def press_button(self):
        print('Nothing happened, money you insert is: {}, but actual price is: {}'.format(
            self.vending_maching.get_money(), self.vending_maching.get_coffee_price()))

    def dispense(self):
        print('Nothing dispensed, money you insert is: {}, but actual price is: {}'.format(
            self.vending_maching.get_money(), self.vending_maching.get_coffee_price()))


class CorrectMoneyState(StateInterface):
    def __init__(self, vending_maching):
        self.vending_maching = vending_maching

    def insert_money(self, money=0):
        print('You can not insert money, because you already insert')

    def eject_money(self):
        print('money returned')
        self.vending_maching.set_state(self.vending_maching.get_no_money_state())

    def press_button(self):
        print('press button')
        self.vending_maching.set_state(self.vending_maching.get_sold_state())

    def dispense(self):
        print('Nothing dispensed, press button first, please')
