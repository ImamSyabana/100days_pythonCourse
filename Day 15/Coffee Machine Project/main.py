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

# print(MENU["espresso"]["ingredients"]["water"]) # line eksperimen

# TODO: 1das
machine_isOn = True

moneyBank = 0
waterReport = resources["water"]
milkReport = resources["milk"]
coffeeReport = resources["coffee"]

while machine_isOn == True:
    order = str(input("What would you like? (espresso/latte/cappucinno): "))

    if order == 'off':
        machine_isOn = False
        break

    if order == 'report':
        print("Water: {waterLeft}".format(waterLeft = waterReport))
        print("Milk: {milkLeft}".format(milkLeft=milkReport))
        print("Coffe: {coffeLeft}".format(coffeLeft=coffeeReport))
        print("Money: ${moneyStored}".format(moneyStored=moneyBank))
        continue

    if order != 'espresso':
        if waterReport < (MENU["{x}".format(x = order)]["ingredients"]["water"]):
            print("Sorry there is not enough water")
        if milkReport < (MENU["{x}".format(x = order)]["ingredients"]["milk"]):
            print("Sorry there is not enough milk")
        if coffeeReport < (MENU["{x}".format(x = order)]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee")

        # ini panjang banget
        if (waterReport < (MENU["{x}".format(x=order)]["ingredients"]["water"]) or milkReport < (
        MENU["{x}".format(x=order)]["ingredients"]["milk"]) or coffeeReport < (
        MENU["{x}".format(x=order)]["ingredients"]["coffee"])):
            continue

    elif order == 'espresso':
        if waterReport < (MENU["{x}".format(x = order)]["ingredients"]["water"]):
            print("Sorry there is not enough water")
        if coffeeReport < (MENU["{x}".format(x = order)]["ingredients"]["coffee"]):
            print("Sorry there is not enough coffee")

        # ini panjang banget
        if (waterReport < (MENU["{x}".format(x=order)]["ingredients"]["water"]) or coffeeReport < (
        MENU["{x}".format(x=order)]["ingredients"]["coffee"])):
            continue

    print("Please insert coins. ")
    quarters_qnt = int(input("How many quarters?: "))
    dimes_qnt = int(input("How many dimes?: "))
    nickels_qnt = int(input("How many nickles?: "))
    pennies_qnt = int(input("How many pennies?: "))

    quarters = quarters_qnt * 0.25
    dimes = dimes_qnt * 0.10
    nickels = nickels_qnt * 0.05
    pennies = pennies_qnt * 0.01

    userMoney = quarters + dimes + nickels + pennies
    orderCost = MENU["{x}".format(x = order)]["cost"]

    if userMoney < orderCost:
        print("Sorry that's not enough money. Money refunded.")
        waterReport = waterReport
        milkReport = milkReport
        coffeeReport = coffeeReport
        moneyBank = moneyBank
        continue

    else:
        if order != 'espresso':
            print("Here is ${changeMoney} in change.".format(changeMoney = round((userMoney - orderCost),2)))
            waterReport = waterReport - (MENU["{x}".format(x = order)]["ingredients"]["water"])
            milkReport = milkReport - (MENU["{x}".format(x=order)]["ingredients"]["milk"])
            coffeeReport = coffeeReport - (MENU["{x}".format(x=order)]["ingredients"]["coffee"])
            moneyBank = moneyBank + orderCost

        elif order == 'espresso':
            print("Here is ${changeMoney} in change.".format(changeMoney=round((userMoney - orderCost), 2)))
            waterReport = waterReport - (MENU["{x}".format(x=order)]["ingredients"]["water"])
            coffeeReport = coffeeReport - (MENU["{x}".format(x=order)]["ingredients"]["coffee"])
            moneyBank = moneyBank + orderCost

        print("Here is your {order} ☕. Enjoy!".format(order=order))

