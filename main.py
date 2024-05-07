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



def check_resource(order, water_resource, milk_resource, coffee_resource):
    '''Takes the values of order, and the current water/milk/coffee resources and check resources sufficient. Returns True(= resources sufficient) or False(= resources insufficient).'''
    if water_resource >= MENU[order]["ingredients"]["water"] and coffee_resource >= MENU[order]["ingredients"]["coffee"]:
        if order != "espresso" and milk_resource >= MENU[order]["ingredients"]["milk"]:
            return True
        elif order == "espresso":
            return True
    else:
        return False



def deduct(order):
    '''Replaces the previous resource values with updated ones after serving each cup of coffee.'''
    resources["water"] -= MENU[order]["ingredients"]["water"]
    resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
    if order == "latte" or order == "cappuccino":
        resources["milk"] -= MENU[order]["ingredients"]["milk"]

def total_insert(order):
    '''Takes the order then calculates all inserted coins and returns its value.'''
    total = 0
    quarter = int(input("Please insert coins.\nhow many quarters?: "))
    total += 0.25 * quarter
    dime = int(input("how many dimes?: "))
    total += 0.10 * dime
    nickel = int(input("how many nickels?: "))
    total += 0.05 * nickel
    penny = int(input("how many pennies?: "))
    total += 0.01 * penny

    cost = MENU[order]["cost"]
    change = round((total - cost), 2)

    if total >= cost:
        deduct(order)
        return f"Here is ${change} change. \nHere is your {order}, enjoy!☕️"
    else:
        return "Sorry. That's not enough money. Money refunded."

def insuff_resource(order, water_resource, coffee_resource, milk_resource):
    if water_resource < MENU[order]["ingredients"]["water"]:
        return "Sorry, there is not enough water."
    elif coffee_resource < MENU[order]["ingredients"]["coffee"]:
        return "Sorry, there is not enough coffee."
    elif milk_resource < MENU[order]["ingredients"]["milk"]:
        return "Sorry, there is not enough milk."





def coffee_machine():
    should_continue = True
    profit = 0
    while should_continue:

        water_resource = resources["water"]
        milk_resource = resources["milk"]
        coffee_resource = resources["coffee"]

        order = input(" What would you like? (espresso/latte/cappuccino): ")
        if order == "report":
            print(f"Water: {water_resource}ml\nMilk: {milk_resource}ml\nCoffee: {coffee_resource}g\n Money: ${profit}")
        elif order == "off":
            should_continue = False
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            make_drink = check_resource(order, water_resource, milk_resource, coffee_resource)
            # print(make_drink)    ###for check, result: OK
            if make_drink:
                if order == "espresso":
                    profit += 1.50
                    print(total_insert("espresso"))
                elif order == "latte":
                    profit += 2.50
                    print(total_insert("latte"))
                elif order == "cappuccino":
                    profit += 3.00
                    print(total_insert("cappuccino"))
            else:
                if order == "espresso":
                    print(insuff_resource("espresso", water_resource, coffee_resource, milk_resource))

                elif order == "latte":
                    print(insuff_resource("latte", water_resource, coffee_resource, milk_resource))

                elif order == "cappuccino":
                    print(insuff_resource("cappuccino", water_resource, coffee_resource, milk_resource))


coffee_machine()
