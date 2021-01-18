from menu_item import MenuItem
from menu_interface import MenuInterface


class DinnerMenu(MenuInterface):
    def __init__(self):
        self._menu_items = {}
        self.add_item('salmon', '340', 'pan-fried salmon')
        self.add_item('whole wheat bread', '50', 'for vegetarian')

    def add_item(self, name, price, description):
        self._menu_items[name] = MenuItem(name, price, description)

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self._menu_items):
            menu_item = list(self._menu_items.values())[self.idx]
            self.idx += 1
            return menu_item
        else:
            raise StopIteration
