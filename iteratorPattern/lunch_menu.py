from menu_item import MenuItem
from menu_interface import MenuInterface


class LunchMenu(MenuInterface):
    def __init__(self):
        self._menu_items = []
        self.add_item('beef', '240', 'pan-fried steak')
        self.add_item('white bread', '50', 'for vegetarian')

    def add_item(self, name, price, description):
        self._menu_items.append(MenuItem(name, price, description))

    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        if self.idx < len(self._menu_items):
            menu_item = self._menu_items[self.idx]
            self.idx += 1
            return menu_item
        else:
            raise StopIteration
