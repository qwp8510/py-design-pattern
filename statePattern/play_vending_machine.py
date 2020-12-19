from vending_machine import VendingMachine


def order_a_coffee(vending_machine):
    vending_machine.insert_money(10)
    vending_machine.press_button()

    print('number of coffee the vending machine have : {}'.format(vending_machine.get_num()))


def order_two_coffee(vending_machine):
    vending_machine.insert_money(10)
    vending_machine.press_button()
    vending_machine.insert_money(10)
    vending_machine.press_button()
    print('number of coffee the vending machine have : {}'.format(vending_machine.get_num()))


def eject_money(vending_machine):
    vending_machine.insert_money(10)
    vending_machine.eject_money()
    print('how much we insert after we eject: {}'.format(vending_machine.get_money()))


def eject_money_fail(vending_machine):
    vending_machine.insert_money(10)
    vending_machine.press_button()
    vending_machine.eject_money()


def main():
    print('===order a coffee===')
    order_a_coffee(VendingMachine(3))
    print('===order two cup of coffee===')
    order_two_coffee(VendingMachine(3))
    print('===eject money===')
    eject_money(VendingMachine(3))
    print('===eject money failed===')
    eject_money_fail(VendingMachine(3))


if __name__ == '__main__':
    main()
