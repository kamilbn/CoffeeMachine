import data
import time

# quarters = 0.25
# dimes = 0.10
# nickles = 0.05
# pennies = 0.01

def payments(action):

    print("Please insert coins")
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickles?: "))
    p = int(input("How many pennies?: "))
    print('─' * 50)
    inserted_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    print(f"Sum of your inserted coins: {inserted_money}")
    if inserted_money < data.MENU[action]['cost']:
        print("You inserted too low coins")
        time.sleep(2)
        return False
    else:
        rest = round(inserted_money - data.MENU[action]['cost'], 2)
        print(f"Here is ${rest} in change")
        return True


def game():
    water = data.resources['water']
    milk = data.resources['milk']
    coffee = data.resources['coffee']
    money = 0
    isEnough = True
    off = False
    while not off:
        print(data.logo)

        print("What would you like? (espresso/latte/cappuccino)")
        for x, y in data.MENU.items():
            print(f"{x} cost ${y['cost']}")
        print('─' * 50)
        print("Others available options:\n'off' - exit\n'report' - shows report about resources\n'restart' - restores resources")

        print('─' * 50)
        option = input("Type what you choose: ").lower()

        if option == "report":
            print("Available resources: ")
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
            time.sleep(3)
        elif option == "off":
            off = True
        elif option == "restart":
            water = data.resources['water']
            milk = data.resources['milk']
            coffee = data.resources['coffee']
            money = 0
            print("Restoring resources...")
            time.sleep(2)
        else:
            if option == "espresso":

                if water < data.MENU['espresso']['ingredients']['water']:
                    print("Sorry there is not enough water")
                    isEnough = False
                elif coffee < data.MENU['espresso']['ingredients']['coffee']:
                    print("Sorry there is not enough coffee")
                    isEnough = False
                else:
                    isEnough = True
                if isEnough == True:
                    pay = payments(option)
                    if pay:
                        water -= data.MENU['espresso']['ingredients']['water']
                        coffee -= data.MENU['espresso']['ingredients']['coffee']
                        money += data.MENU['espresso']['cost']
                        print("Here is your espresso. Enjoy")
                        isEnough = True
                        time.sleep(3)
            elif option == "latte":
                if water < data.MENU['latte']['ingredients']['water']:
                    print("Sorry there is not enough water")
                    isEnough = False
                elif milk < data.MENU['latte']['ingredients']['milk']:
                    print("Sorry there is not enough milk")
                    isEnough = False
                elif coffee < data.MENU['latte']['ingredients']['coffee']:
                    print("Sorry there is not enough coffee")
                    isEnough = False
                else:
                    isEnough = True
                if isEnough == True:
                    pay = payments(option)
                    if pay:
                        water -= data.MENU['latte']['ingredients']['water']
                        milk -= data.MENU['latte']['ingredients']['milk']
                        coffee -= data.MENU['latte']['ingredients']['coffee']
                        money += data.MENU['latte']['cost']
                        print("Here is your latte. Enjoy")
                        isEnough = True
                        time.sleep(3)

            elif option == "cappuccino":
                if water < data.MENU['cappuccino']['ingredients']['water']:
                    print("Sorry there is not enough water")
                    isEnough = False
                elif milk < data.MENU['cappuccino']['ingredients']['milk']:
                    print("Sorry there is not enough milk")
                    isEnough = False
                elif coffee < data.MENU['cappuccino']['ingredients']['coffee']:
                    print("Sorry there is not enough coffee")
                    isEnough = False
                else:
                    isEnough = True
                if isEnough == True:
                    pay = payments(option)
                    if pay:
                        water -= data.MENU['cappuccino']['ingredients']['water']
                        milk -= data.MENU['cappuccino']['ingredients']['milk']
                        coffee -= data.MENU['cappuccino']['ingredients']['coffee']
                        money += data.MENU['cappuccino']['cost']
                        print("Here is your cappuccino. Enjoy")
                        isEnough = True
                        time.sleep(3)

            else:
                print("\nYou typed wrong value.")
                time.sleep(1)


game()
