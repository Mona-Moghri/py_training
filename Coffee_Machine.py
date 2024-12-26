
#Coffee Machine
# challenge is i should write coffee machine with class. this is the next taxt that i should deal with

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

MONEY_IN_MACHINE= 0


def report_resources(resources, money_in_machine):
    """display current resources and total money collected from user"""
    for ingredient, amount in resources.items():   #used with dictionaries. It allows you to loop through both keys and their corresponding values
        if ingredient in ["water", "milk"]:
            print(f"{ingredient}:{amount}ml")
        elif ingredient == "coffee":
            print(f"{ingredient}:{amount}g")
    print(f"Money: ${money_in_machine: }")


def process_coin(cost):
    """calculate does coin enough for specefic coffee and return reminder of coin"""
    print("Please insert coins.")
    quarters= float(input("how many quarters?: ")) *0.25
    dimes = float(input("how many dimes?: ")) *0.10
    nickles = float(input("how many nickles? ")) *0.05
    pennies = float(input("how many pennies?: ")) *0.01

    #calculate total money inserted
    total_coin= quarters + dimes + nickles + pennies

    if total_coin < cost:
        print("you are not enough coin, money refunded")
        return -1, 0 #-1 indicates falure, no money to add to the machine
    else:
        coin_remain= total_coin - cost
        print(f"Here is ${coin_remain: .2f} in change.")
        return cost, total_coin - coin_remain


def make_coffee(choice, resources, money_in_machine):
    """check and update resources for specific coffee and how much money need it"""
    coffee_user_choose=MENU[choice]
    ingredient_for_each_coffee= coffee_user_choose["ingredients"]
    cost= coffee_user_choose["cost"]

    for material, needed in ingredient_for_each_coffee.items():
        if resources.get(material, 0) < needed:   #use get if the material key deose not exist in the resources dictionary. get allow the program return 0 which we choose instead of error
            print(f"Sorry there is not enough water {material}.")
            return money_in_machine
    cost_to_add, coin_to_add= process_coin(cost)
    if cost_to_add == -1:
        return money_in_machine

    for material, needed in ingredient_for_each_coffee.items():
        resources[material] -= needed
    money_in_machine += coin_to_add
    print(f"Here is your {choice} ☕️. Enjoy!")

    return money_in_machine

while True:
    CHOOSE_YOUR_COFFEE = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if CHOOSE_YOUR_COFFEE == "report":
        report_resources(resources, MONEY_IN_MACHINE)
    elif CHOOSE_YOUR_COFFEE in MENU:
        MONEY_IN_MACHINE= make_coffee(CHOOSE_YOUR_COFFEE, resources, MONEY_IN_MACHINE)
    elif CHOOSE_YOUR_COFFEE == "off":
        print("turning off the coffee machine.")
        break
    else:
        CHOOSE_YOUR_COFFEE = input("What would you like? (espresso/latte/cappuccino): ").lower()