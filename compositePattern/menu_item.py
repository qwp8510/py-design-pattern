from menu_component import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, item_name, price, description):
        self.item_name = item_name
        self.price = price
        self.description = description

    def get_item_name(self):
        return self.item_name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def show(self):
        print(
            self.get_item_name(),
            self.get_price(),
            self.get_description()
        )
        print('------------------')
