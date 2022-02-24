from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
shouldContinue = True

coffeemaker.report()
moneymachine.report()

while(shouldContinue):
    choice = input(f'What would you like? {menu.get_items()}: ')
    if choice.lower() == 'report':
        coffeemaker.report()
        moneymachine.report()
        # shouldContinue = False
        # break
    elif choice.lower() == 'off':
       shouldContinue = False
       break
    else:
        # isResourceSufficient = coffeemaker.is_resource_sufficient(drink)
        # if not isResourceSufficient:
        #     shouldContinue = False
        #     break
        # #print(drink)
        # isMoneySufficient = moneymachine.make_payment(drink.cost)
        # if isResourceSufficient and isMoneySufficient:
        #     coffeemaker.make_coffee(drink)
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)

