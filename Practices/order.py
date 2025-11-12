#VY 2nd Order Up
import time
#create four dictionaries, one for each of these categories: drinks, sides, and main meals
#each dictionary must have at least 4 different menu item, and each menu item must have a cost. Do a nested dictionary for this.
drinks = {
    #item as key: price as value
    "Water": 0,
    "Coke": 0.99,
    "Sprite": 0.50,
    "Fanta": 0.80
}
mains = {
    "Pizza": 5.99,
    "Cheeseburger": 7.99,
    "Hamburger": 8.99,
    "Chicken tenders": 6.99
}
sides = {
    "Fries": 3.50,
    "Pretzels": 3.99,
    "Chips": 1.99,
    "Salad": 2.99,
}

#print the full menu by looping through the dictionary. Make a function for this, and call it if the user wants to see the menu.
def view_menu():
    print("Drinks:")
    for drink in drinks.keys():
        print(f"\t{drink} is {drinks[drink]}")

    print("Main meals:")
    for meal in mains.keys():
        print(f"\t{meal} is {mains[meal]}")

    print("Sides:")
    for side in sides.keys():
        print(f"\t{side} is {sides[side]}")


#make a function for ordering drinks
def order_drink():
    while True:
        user_drink = input("What drink would you like?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_drink.capitalize() in sides or user_drink.capitalize() in mains:
            print("Please choose a drink as of right now.")
        #give the user the option to say they aren't ready yet.
        elif user_drink == "n":
            print("Let me know when you are ready to order.")
            break
        #if the drink is not found in the dictionary, tell them to order again
        elif user_drink.capitalize() not in drinks:
            print("Sorry, that is not on our menu. Please choose an available option.")
        else:
            return user_drink

#make a function for ordering a main
def order_main():
    while True:
        user_main = input("What main meal do you want?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_main.capitalize() in sides or user_main.capitalize() in drinks:
            print("Please choose a main meal as of right now.")
        #give the user the option to say they aren't ready yet.
        elif user_main == "n":
            print("Alright! Let me know when you're ready to order.")
            break
        elif user_main.capitalize() not in mains:
            print("Sorry, that is not on our menu. Please choose an available option.")
        else:
            return user_main

#make a function for ordering sides
def first_side():
    two_sides = False
    while True:
        first_side = input("What will your first side be?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if first_side.capitalize() in drinks or first_side.capitalize() in mains:
            print("Please choose a side as of right now.")
        #give the user the option to say they aren't ready yet.
        elif first_side == "n":
            print("Okay. Let me know when you want to order.")
            continue
        #if the side is not found in the dictionary, tell them to order again.
        elif first_side.capitalize() not in sides:
            print("Sorry, that is not on our menu. Please choose an available option.")
        else:
            return first_side

def second_side():
    #ask the user if they want a second one.
    ask_second = input("Would you like a second side?(y/n): ")
    if ask_second == "y":
        while True:
            second_side = input("What will your second side be?(n if you're not ready): ")
            #if the item is on a different dictionary, print something else and tell them to order again.
            if second_side.capitalize() in drinks or second_side.capitalize() in mains:
                print("Please choose a side as of right now.")
            #give the user the option to say they aren't ready yet.
            elif second_side == "n":
                print("Let me know when you know what you want.")
                break
            #if the side is not found in the dictionary, tell them to order again.
            elif second_side.capitalize() not in sides:
                print("Sorry, that is not on our menu. Please choose an available option.")
            else:
                return second_side
    elif ask_second == "n":
        print("Alright then.")
        return None
        
#make a function for adding up all values
def add_total(drink, main, one_side, second_side):
    total = drinks[drink] + mains[main] + sides[one_side]
    if sides[second_side]:
        total += sides[second_side]
    return total


#greet the user and show them the menu.
print("Hello there!")

while True:
    #ask the user if they're ready to order or not yet
    user_choice = input("Do you want to order or see the menu?(o/m): ")
    if user_choice == "o":
        #get all of the items(the keys) that the user ordered, get their price (the values) and add it all up
        drink_choice = order_drink()
        main_choice = order_main()
        first_side_choice = first_side()
        second_side_choice = second_side()
        if second_side_choice:
            final_total = add_total(drink_choice, main_choice, first_side_choice, second_side_choice)
            print(f"Your order: \n\tDrink: {drink_choice} \n\tMain Course: {main_choice} \n\tSide Dishes: \n\t\t{first_side_choice} \n\t\t{second_side_choice} \nTotal Cost: ${final_total}")
        else:
            final_total = add_total(drink_choice, main_choice, first_side_choice, 0)
            print(f"Your order: \n\tDrink: {drink_choice} \n\tMain Course: {main_choice} \n\tSide Dishes: \n\t\t{first_side_choice} \nTotal Cost: ${final_total}")
        break
    elif user_choice == "m":
        print("Here is our menu.")
        view_menu()
        time.sleep(3)
    else:
        print("Sorry, I didn't get that.")


#finally, print all of the items(set as keys) and print out the price of the order.







#wawa :(