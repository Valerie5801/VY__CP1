#VY 2nd Combat Program
import random

fighters = { #change numbers idk what im doing, may have to change this into variables based on logic
    "Knight":{
        "option_num" : 1,
        "health" : 30,
        "defense" : 14,
        "attack" : 10,
        "damage" : 7
    },
    "Mage":{
        "option_num" : 2,
        "health" : 25,
        "defense" : 14,
        "attack" : 15,
        "damage" : 5
    },
    "Rogue":{
        "option_num" : 3,
        "health" : 15,
        "defense" : 10,
        "attack" : 30,
        "damage" : 9
    }
}

rival_fighter = random.randint(1, 3)
if rival_fighter == 1:
    
    print("Your rival is a Knight.")
elif rival_fighter == 2:
    print("Your rival is a Mage.")
elif rival_fighter == 3:
    print("Your rival is a Rogue.")

def user_combat():
    print("Action time!")
    print("1. Normal Attack \n2. Wild Attack(you take a little bit of damage) \n3. Heal(by 6 points) \n4. Guard(raise your defense by 3)")
    user_action = input("What would you like to do?: ")
    if user_fighter == "1":
        if user_action == "1":
            print("user knight attacked")
        elif user_action == "2":
            print("user knight furiously attacked")
        elif user_action == "3":
            
    elif user_fighter == "2":
        print("user knight furiously attacked")
    elif user_fighter == "3":
        print("yum")

print("Hello! This a combat training simulator.")
name = input("First off, what is your name?: ")
print(f"Nice to meet you, {name}! \nNow, here are your options for the classes: \n1 for a Knight \n2 for a Mage \n3 for a Rogue.")
user_fighter = input("Choose a class: ")
print("Awesome! Now...\n")

if user_fighter == "1":
    print(f"You are a Knight. \nYour stats are: \nHealth: {fighters["Knight"]["health"]} \nDefense: {fighters["Knight"]["defense"]} \nAttack: {fighters["Knight"]["attack"]} \nDamage: {fighters["Knight"]["damage"]}")
elif user_fighter == "2":
    print(f"You are a Mage. \nYour stats are: \nHealth: {fighters["Mage"]["health"]} \nDefense: {fighters["Mage"]["defense"]} \nAttack: {fighters["Mage"]["attack"]} \nDamage: {fighters["Mage"]["damage"]}")
elif user_fighter == "3":
    print(f"You are a Rogue. \nYour stats are: \nHealth: {fighters["Rogue"]["health"]} \nDefense: {fighters["Rogue"]["defense"]} \nAttack: {fighters["Rogue"]["attack"]} \nDamage: {fighters["Rogue"]["damage"]}")

print("\nYour rival seems ready to battle!")

