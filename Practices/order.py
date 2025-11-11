#VY 2nd Order Up

#create four dictionaries, one for each of these categories: drinks, sides, and main meals
#each dictionary must have at least 4 different menu item, and each menu item must have a cost. Do a nested dictionary for this.
drinks = {
    #item as key: price as value
    "Water": 0,
    "Coke": 0.99,
    "Sprite": 0.50,
    "Fanta": 0.80
}
sides = {
    "Fries": 3.50,
    "Pretzels": 3.99,
    "Chips": 1.99,
    "Salad": 2.99,
}
mains = {
    "Pizza": 5.99,
    "Cheeseburger": 7.99,
    "Hamburger": 8.99,
    "Chicken tenders": 6.99
}

#print the full menu by looping through the dictionary. Make a function for this, and call it if the user wants to see the menu.
def view_menu():
    print("Drinks:")
    for drink in drinks.keys():
        print(f"\t{drink} is {drinks[drink]}")

    print("Sides:")
    for side in sides.keys():
        print(f"\t{side} is {sides[side]}")
    
    print("Main meals:")
    for meal in mains.keys():
        print(f"\t{meal} is {mains[meal]}")


#make a function for ordering.
def ordering():
    while True:
        user_drink = input("What drink would you like?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_drink.capitalize() in sides or user_drink.capitalize() in mains:
            print("Please choose a drink as of right now.")
        #if the drink is not found in the dictionary, tell them to order again
        elif user_drink.capitalize() not in drinks:
            print("Sorry, that is not on our menu. Please choose an available option.")
            #give the user the option to say they aren't ready yet.
        elif user_drink == "n":
            print("Let me know when you are ready to order.")
            break
        else:
            break

    #ask the user what main they want
    while True:
        user_main = input("What main meal do you want?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if user_main.capitalize() in sides or user_main.capitalize() in drinks:
            print("Please choose a main meal as of right now.")
        elif user_main.capitalize() not in mains:
            print("Sorry, that is not on our menu. Please choose an available option.")
            #give the user the option to say they aren't ready yet.
        elif user_main == "n":
            print("Alright! Let me know when you're ready to order.")
            break
        else:
            break

    #ask the user what their first side is
    while True:
        first_side = input("What will your first side be?(n if you're not ready): ")
        #if the item is on a different dictionary, print something else and tell them to order again.
        if first_side.capitalize() in drinks or first_side.capitalize() in mains:
            print("Please choose a side as of right now.")
        #if the side is not found in the dictionary, tell them to order again.
        elif first_side.capitalize() not in sides:
            print("Sorry, that is not on our menu. Pleaes chooes an available option.")
        #give the user the option to say they aren't ready yet.
        elif first_side == "n":
            print("Okay. Let me know when you want to order.")
            break
        else:
            break

    #ask the user if they want a second one.
    ask_second = input("Would you like a second side?(y/n): ")
    if ask_second == "y":
        while True:
            second_side = input("What will you rsecond side be?(n if you're not ready): ")
            #if the item is on a different dictionary, print something else and tell them to order again.
            if second_side.capitalize() in drinks or second_side.capitalize() in mains:
                print("Please choose a side as of right now.")
            #if the side is not found in the dictionary, tell them to order again.
            elif second_side.capitalize() not in sides:
                print("Sorry, that is not on our menu. Pleaes chooes an available option.")
            #give the user the option to say they aren't ready yet.
            elif second_side.capitalize() == "n":
                print("Let me know when you know what you want.")
                break
            else:
                break
    elif ask_second == "n":
        print("Alright then.")

#greet the user and show them the menu.
print("Hello there!")
print("Here is our menu.\n")
view_menu()


#get all of the items(the keys) that the user ordered, get their price (the values) and add it all up

#finally, print all of the items(set as keys) and print out the price of the order.







#wawa :(