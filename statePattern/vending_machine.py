from state import SoldState, SoldOutState, NoMoneyState, HasMoneyState


class VendingMachine():
    def __init__(self, coffee_num=10):
        self.state = SoldOutState(self)
        self.money = 0
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)
        self.no_money_state = NoMoneyState(self)
        self.has_money_state = HasMoneyState(self)
        self.coffee_num = coffee_num
        if self.coffee_num:
            self.state = NoMoneyState(self)

    def insert_money(self, money):
        self.set_money(money)
        self.state.insert_money(money)

    def eject_money(self):
        self.set_money(0)
        self.state.eject_money()

    def press_button(self):
        self.state.press_button()
        self.state.dispense()

    def set_state(self, state):
        self.state = state

    def release(self):
        print('your coffee is coming')
        if self.coffee_num > 0:
            self.coffee_num -= 1

    def get_sold_state(self):
        return self.sold_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_no_money_state(self):
        return self.no_money_state

    def get_has_money_state(self):
        return self.has_money_state

    def get_num(self):
        return self.coffee_num

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money
