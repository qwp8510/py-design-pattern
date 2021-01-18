class Waiter():
    def __init__(self, launch_menu, dinner_menu):
        self.launch_menu = launch_menu
        self.dinner_menu = dinner_menu

    def show_menu(self):
        print('--lunch--')
        self._show(self.launch_menu)
        print('--dinner--')
        self._show(self.dinner_menu)

    def _show(self, iterator):
        for item in iterator:
            print(
                item.get_item_name(),
                item.get_price(),
                item.get_description()
            )
