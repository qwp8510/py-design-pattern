from base_pizza import Pizza


class AmericaCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name='America style Cheese pizza',
            dough='Thin Crust Dough',
            sauce='Marinara sauce')
        self.toppings.append('Grated Raggiano cheese')


class AmericaVeggiePizza(Pizza):
    def __init__(self):
        super().__init__(
            name='America style Veggie pizza',
            dough='Thin Crust Dough',
            sauce='Veggie sauce')
        for topping in ['pickle', 'cucumber', 'onion', 'thousand island dressing']:
            self.toppings.append(topping)


class TaiwanCheesePizza(Pizza):
    def __init__(self):
        super().__init__(
            name='Taiwan style Cheese pizza',
            dough='Thin Crust Dough',
            sauce='Marinara sauce')
        self.toppings.append('Grated Raggiano cheese')


class UnknownPizza(Pizza):
    def __init__(self):
        super().__init__(name='Unknown pizza', dough='', sauce='')
