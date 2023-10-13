from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
item = MenuItem

thirsty = True
while thirsty:
    answer = input("what would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "off":
        print(f"Coffee machine needs some rest. MACHINE {answer}")
        thirsty = False
    elif answer == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(answer)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
