from breakfast_shop import HappyBreakfastShop
from components.characters import OfficeWorker


def main():
    character = OfficeWorker('Daniel')
    HappyBreakfastShop(character).eat('Big Mac meal')


if __name__ == "__main__":
    main()
