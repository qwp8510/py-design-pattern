from state import SoldState, SoldOutState, NoMoneyState, HasMoneyState, CorrectMoneyState


class VendingMachine():
    def __init__(self, coffee_num=10, coffee_price=10):
        self._money = 0
        self._sold_state = SoldState(self)
        self._sold_out_state = SoldOutState(self)
        self._no_money_state = NoMoneyState(self)
        self._has_money_state = HasMoneyState(self)
        self._correct_money_state = CorrectMoneyState(self)
        self._coffee_num = coffee_num
        self._coffee_price = coffee_price
        self._state = self._sold_out_state
        if self._coffee_num > 0:
            self._state = self._no_money_state

    def insert_money(self, money):
        self.set_money(money)
        self._state.insert_money(money)

    def eject_money(self):
        self.set_money(0)
        self._state.eject_money()

    def press_button(self):
        self._state.press_button()
        self._state.dispense()

    def set_state(self, state):
        self._state = state

    def release(self):
        print('your coffee is coming')
        if self._coffee_num > 0:
            self._coffee_num -= 1

    def get_sold_state(self):
        return self._sold_state

    def get_sold_out_state(self):
        return self._sold_out_state

    def get_no_money_state(self):
        return self._no_money_state

    def get_has_money_state(self):
        return self._has_money_state

    def get_correct_money_state(self):
        return self._correct_money_state

    def get_num(self):
        return self._coffee_num

    def get_money(self):
        return self._money

    def set_money(self, money):
        self._money = money

    def get_coffee_price(self):
        return self._coffee_price

    def check_money_correct(self):
        return self.get_money() == self._coffee_price
