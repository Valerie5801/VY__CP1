#VY 2nd Order Up
import time
#create three dictionaries, one for each of these categories: drinks, sides, and main meals
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
        user_drink = input("What drink would you like?(capitalize your order): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_drink.capitalize() in sides or user_drink.capitalize() in mains:
            print("Please choose a drink as of right now.")
        #if the drink is not found in the dictionary, tell them to order again
        elif user_drink not in drinks:
            print("Sorry.")
            if user_drink.capitalize() in drinks: #fail safe in case user didn't capitalize because keys are case-sensitive
                print("You need to capitalize.")
            else: #in case the user typed in something that isn't on the menu
                print("That drink is not on our menu. Please order again.")
        else:
            return user_drink

#make a function for ordering a main
def order_main():
    while True:
        user_main = input("What main meal do you want?(capitalize your order): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_main.capitalize() in sides or user_main.capitalize() in drinks:
            print("Please choose a main meal as of right now.")
        #if the main is not found in the dictionary, tell them to order again
        elif user_main not in mains:
            print("Sorry.")
            if user_main.capitalize() in mains: #fail safe in case user didn't capitalize because keys are case-sensitive
                print("You need to capitalize.")
            else: #in case the user typed something that isn't on the menu
                print("That item is not on our menu. Please order again.")
        else:
            return user_main

#make a function for ordering one side
def first_side():
    while True:
        first_side = input("What will your first side be?(capitalize your order): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if first_side.capitalize() in drinks or first_side.capitalize() in mains:
            print("Please choose a side as of right now.")
        #if the side is not found in the dictionary, tell them to order again
        elif first_side not in sides:
            print("Sorry.")
            if first_side.capitalize() in sides: #fail safe in case user didn't capitalize because keys are case-sensitive
                print("You need to capitalize.")
            else: #in case the user typed something that isn't on the menu
                print("That side is not on our menu. Please order again.")
        else:
            return first_side

#make a function for ordering a second side
def second_side():
    while True:
        second_side = input("What will your second side be?(capitalize your order): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if second_side.capitalize() in drinks or second_side.capitalize() in mains:
            print("Please choose a side as of right now.")
        #if the item is not found in the dictionary, tell them to order again
        elif second_side not in sides:
            print("Sorry.")
            if second_side.capitalize() in sides: #fail safe in case user didn't capitalize because keys are case-sensitive
                print("You need to capitalize.")
            else: #in case the user typed something that isn't on the menu
                print("That side is not on our menu. Please order again.")
        else:
            return second_side
        
#make a function for adding up all values
def add_total(drink, main, one_side, second_side):
    total = drinks[drink] + mains[main] + sides[one_side] + sides[second_side]
    return total


#greet the user and show them the menu.
print("Hello there!")

while True:
    #ask the user if they're ready to order or not yet
    user_choice = input("Do you want to order or see the menu?(o/m): ")
    if user_choice == "o":
        #get all of the items(the keys) that the user ordered, get their price (the values) and add it all up
        drink_choice = order_drink() #set them to variables so their values don't change
        main_choice = order_main()
        first_side_choice = first_side()
        second_side_choice = second_side()
        #add all of the prices up and print out the order
        final_total = add_total(drink_choice, main_choice, first_side_choice, second_side_choice)
        print(f"Your order: \n\tDrink: {drink_choice} \n\tMain: {main_choice} \n\tSide Dishes: \n\t\t{first_side_choice} \n\t\t{second_side_choice} \nTotal Cost: ${round(final_total, 2)}")
        break
    elif user_choice == "m":
        #print the menu
        print("Here is our menu.")
        view_menu()
        time.sleep(2)
    else:
        #stupid proof it so no other orders can get through
        print("Sorry, I didn't get that.")