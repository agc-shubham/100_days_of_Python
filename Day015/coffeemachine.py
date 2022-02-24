MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
shouldContinue = True

def check_resources(choice,ingredient):
    Requested = MENU[choice]['ingredients']
    if(resources[ingredient]>= Requested[ingredient]):
        return True
    else:
        print(f'Sorry there is not enough {ingredient}.')
        global shouldContinue 
        shouldContinue = False
        return False



def processCoins(choice):
    moneyCollected = int(input('Enter the number of quarters: '))*0.25
    moneyCollected += int(input('Enter the number of dimes: '))*0.10
    moneyCollected += int(input('Enter the number of nickels: '))*0.05
    moneyCollected += int(input('Enter the number of pennies: '))*0.01
    cost = MENU[choice]['cost']
    if(moneyCollected>=cost):
        print(f'Transaction Sucessful \nHere\'s ${moneyCollected-cost} dollars in change. ')
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False
def make_coffee(choice):
    Requested = MENU[choice]['ingredients'] 
    if(choice.lower() == "espresso"):
        resources['water'] -= Requested['water']
        resources['coffee'] -= Requested['coffee']
    else:
        resources['water'] -= Requested['water']
        resources['coffee'] -= Requested['coffee']
        resources['milk'] -= Requested['milk']
    global profit
    profit += MENU[choice]['cost']


while(shouldContinue):
    Choice = input('What would you like? (espresso/latte/cappuccino): ')
    if Choice.lower() == 'off':
       shouldContinue = False
       break
    elif Choice.lower() == 'report':
        print(f'Water: {resources["water"]}, Milk: {resources["milk"]}, Coffee: {resources["coffee"]}, Money: {profit}')
        shouldContinue = False
        break
    else:
       if(Choice.lower() == "espresso"):
           isEnoughResource =  check_resources(Choice,'water') and  check_resources(Choice,'coffee')
           if(not isEnoughResource):
               break
       else:
           isEnoughResource =  check_resources(Choice,'water') and check_resources(Choice,'milk') and check_resources(Choice,'coffee')
           if(not isEnoughResource):
               break 
       #print(isEnoughResource)
       if processCoins(Choice) and isEnoughResource:
           make_coffee(Choice)
           print(f'Here is your {Choice} Enjoy!')