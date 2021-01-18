from menu import Menu
from menu_item import MenuItem
from waiter import Waiter


def main():
    all_menus = Menu('All', 'it is all menu')
    lunch_menu = Menu('Lunch', 'it is lunch menu')
    dinner_menu = Menu('Dinner', 'it is dinner menu')
    drink_menu = Menu('Drink', 'it is drink menu')
    dessert_menu = Menu('Dessert', 'it is dessert menu')

    all_menus.add_child(lunch_menu)
    all_menus.add_child(dinner_menu)
    lunch_menu.add_child(MenuItem('beef', '240', 'pan-fried steak'))
    lunch_menu.add_child(drink_menu)
    drink_menu.add_child(MenuItem('milk tea', '50', 'milk tea without sugar'))
    dinner_menu.add_child(MenuItem('salmon', '340', 'pan-fried salmon'))
    dinner_menu.add_child(MenuItem('whole wheat bread', '50', 'for vegetarian'))
    dinner_menu.add_child(dessert_menu)
    dessert_menu.add_child(MenuItem('Waffle', '100', 'delicious'))
    waiter = Waiter(all_menus)
    waiter.show_menu()


if __name__ == "__main__":
    main()
