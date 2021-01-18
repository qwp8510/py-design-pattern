from menu_item import MenuItem
from iterators import DinnerIterator
from menu_interface import MenuInterface


class DinnerMenu(MenuInterface):
    def __init__(self):
        self._menu_items = {}
        self.add_item('salmon', '340', 'pan-fried salmon')
        self.add_item('whole wheat bread', '50', 'for vegetarian')

    def add_item(self, name, price, description):
        self._menu_items[name] = MenuItem(name, price, description)

    @property
    def item(self):
        return DinnerIterator(self._menu_items)
