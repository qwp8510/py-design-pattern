class HappyBreakfastShopCashier():
    MEAL = {'Big Mac meal': 120}

    def check(self, meal):
        """ Implement check behavior """
        print('your {} is {}'.format(meal, self.MEAL.get(meal, 'Unrecognized meal')))
