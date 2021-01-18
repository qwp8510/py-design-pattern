class Waiter():
    def __init__(self, launch_menu, dinner_menu):
        self.launch_menu = launch_menu
        self.dinner_menu = dinner_menu

    def show_menu(self):
        print('--lunch--')
        self._show(self.launch_menu.item)
        print('--dinner--')
        self._show(self.dinner_menu.item)

    def _show(self, iterator):
        while(iterator.has_next()):
            menu_item = iterator.next()
            print(
                menu_item.get_item_name(),
                menu_item.get_price(),
                menu_item.get_description()
            )
