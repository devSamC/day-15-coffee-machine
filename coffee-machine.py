

menu = {
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
            "water": 500,
            "milk": 100,
            "coffee": 24,

        },
        "cost": 3,
    }

}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def going_for_maintance():
    print("Turning off and refilling machine!")
    return False


def process_choice(coffee_decision, current_resources):
    if coffee_decision == "report":
        print(f"Water: {current_resources['water']}\nMilk: {current_resources['milk']}\nCoffee: {current_resources['coffee']}\nMoney: {current_resources['money']}")
        main(current_resources)
    elif coffee_decision == "off":
        return going_for_maintance()
    else:
        water_remaining = current_resources["water"] - menu[coffee_decision]["ingredients"]["water"] 
        milk_remaining = current_resources["milk"] - menu[coffee_decision]["ingredients"]["milk"] 
        coffee_remaining = current_resources["coffee"] - menu[coffee_decision]["ingredients"]["coffee"] 

        print(f"water: {water_remaining}, milk: {milk_remaining}, coffee: {coffee_remaining}")

        if water_remaining > 0 and milk_remaining > 0 and coffee_remaining > 0:
            new_resources = {
                "water": water_remaining,
                "milk": milk_remaining,
                "coffee": coffee_remaining,
                "money": current_resources["money"],
            }
            return new_resources
        else:
            print("aint got enough resources for that chief")
            return going_for_maintance()

def ask_for_money(coffee_decision, resources):
    print(f"That will be ${menu[coffee_decision]['cost']} please")
    print("Please insert coins: ")
    quarters = int(input("How many quarters: ")) * 25
    dimes = int(input("How many dimes: ")) * 10
    nickels = int(input("How many nickels: ")) * 5
    pennies = int(input("How many pennies: "))

    total_in_dollars = (quarters + dimes + nickels + pennies) / 100
    coffee_cost = menu[coffee_decision]['cost']

    if total_in_dollars >= coffee_cost:
        print(f"Thats a total of ${total_in_dollars} leaving you with ${round(total_in_dollars - coffee_cost,2)} change")
        resources['money'] += coffee_cost
        return resources
    else: 
        print(f"Not enough Money! refunding {total_in_dollars} please try again")

        

def main(current_resources):
    continue_service = True
    coffee_decision = input("What coffee would you like? Cappuccino, Latte or Espresso?: ").lower()
    check = process_choice(coffee_decision, current_resources)
    
    while continue_service:
        if not check:
            current_resources = resources
            continue_service = False
        else:
            new_resources = check
            current_resources = ask_for_money(coffee_decision, new_resources)
            if resources["money"] == current_resources["money"]:
                continue_service = False
            else:
                print(f"Here is your {coffee_decision} enjoy! ")
                continue_service = False
    print(current_resources)
    main(current_resources)



                
            
            



    
    



main(resources)

