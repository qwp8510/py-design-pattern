from decorator import Espresso, DarkRoast
from wrapper import Mocha, Whip, Milk


def main():
    beverage = DarkRoast()
    mocha_beverage = Mocha(beverage)
    double_mocha_beverage = Mocha(mocha_beverage)
    whip_double_mocha_beverage = Whip(double_mocha_beverage)
    print('order : {}, and cost {}'.format(
        whip_double_mocha_beverage.get_description(),
        whip_double_mocha_beverage.cost()))


if __name__ == '__main__':
    main()
