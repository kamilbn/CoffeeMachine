import data


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
    inserted_money = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    if inserted_money < data.MENU[action]['cost']:
        print("You inserted too low coins")
        return False
    else:
        rest = round(inserted_money - data.MENU[action]['cost'], 2)
        print(f"Your money: ${inserted_money}. Here is ${rest} in change")
        return True


def game():
    water = data.resources['water']
    milk = data.resources['milk']
    coffee = data.resources['coffee']
    money = 0  # money = inserted coins - price of coffee
    isEnough = True
    off = False
    while not off:
        #   option report allow you to check the resources of ths machine
        for x,y in data.MENU.items():
            print(f"{x} cost ${y['cost']}")
        option = input("What would you like? (espresso/latte/cappuccino): ")

        if option == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
        elif option == "off":
            off = True
        elif option == "restart":
            water = data.resources['water']
            milk = data.resources['milk']
            coffee = data.resources['coffee']
            money = 0  # money = inserted coins - price of coffee
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

            else:
                print("You typed wrong value.")

        # if (option == "espresso" or option == "latte" or option == "cappuccino") and isEnough:


game()


