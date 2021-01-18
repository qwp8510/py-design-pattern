from menu_item import MenuItem
from iterators import LunchIterator
from menu_interface import MenuInterface


class LunchMenu(MenuInterface):
    def __init__(self):
        self._menu_items = []
        self.add_item('beef', '240', 'pan-fried steak')
        self.add_item('white bread', '50', 'for vegetarian')

    def add_item(self, name, price, description):
        self._menu_items.append(MenuItem(name, price, description))

    @property
    def item(self):
        return LunchIterator(self._menu_items)
