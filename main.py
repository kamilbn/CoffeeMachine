import data
from data import *
water = data.resources['water']
milk = data.resources['milk']
coffee = data.resources['coffee']
money = 0


def resources():
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01


def choice(action):
    if action == "report":
        return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}"


#   option report allow you to check the resources of ths machine
option = input("What would you like? (espresso/latte/cappuccino): ")
print(choice(option))
