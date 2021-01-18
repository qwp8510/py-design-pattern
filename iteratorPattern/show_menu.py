from waiter import Waiter
from lunch_menu import LunchMenu
from dinner_menu import DinnerMenu


def main():
    waiter = Waiter(LunchMenu(), DinnerMenu())
    waiter.show_menu()


if __name__ == "__main__":
    main()
