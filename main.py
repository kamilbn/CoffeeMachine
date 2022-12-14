import data


# def choice(action, a_money, a_water, a_milk, a_coffee):
#     if action == "espresso":
#
#         a_water -= data.MENU['espresso']['ingredients']['water']
#         a_coffee -= data.MENU['espresso']['ingredients']['coffee']
#
#         return f"Here is your expresso Enjoy! ", a_water, a_coffee


water = data.resources['water']
milk = data.resources['milk']
coffee = data.resources['coffee']
money = 0  # money = inserted coins - price of coffee


# quarters = 0.25
# dimes = 0.10
# nickles = 0.05
# pennies = 0.01


#   TODO How to create impact to variables from this function to global dictionary
def game():
    off = False
    while not off:
        #   option report allow you to check the resources of ths machine
        option = input("What would you like? (espresso/latte/cappuccino): ")
        # TODO Create exception if you type different word without any options, causo to crash program
        #  TODO Create the check if you have resources for this coffee
        if option == "report":
            print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
        elif option == "off":
            off = True
        else:
            if option == "espresso":

                water -= data.MENU['espresso']['ingredients']['water']
                coffee -= data.MENU['espresso']['ingredients']['coffee']
                money += data.MENU['espresso']['cost']
            elif option == "latte":
                water -= data.MENU['latte']['ingredients']['water']
                milk -= data.MENU['latte']['ingredients']['milk']
                coffee -= data.MENU['latte']['ingredients']['coffee']
                money += data.MENU['latte']['cost']
            elif option == "cappuccino":
                water -= data.MENU['cappuccino']['ingredients']['water']
                milk -= data.MENU['cappuccino']['ingredients']['milk']
                coffee -= data.MENU['cappuccino']['ingredients']['coffee']
                money += data.MENU['cappuccino']['cost']
            print("Please insert coins")
            q = int(input("How many quarters?: "))
            d = int(input("How many dimes?: "))
            n = int(input("How many nickles?: "))
            p = int(input("How many pennies?: "))
            inserted_money = q*0.25+d*0.10+n*0.05+p*0.01
            rest = round(inserted_money - data.MENU['espresso']['cost'], 2)
            # TODO Calculate rest by inserted coins - price and result the rest
            print(f"Your money: {inserted_money}. Here is ${rest} in change")


game()


