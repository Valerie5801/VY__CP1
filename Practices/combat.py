#VY 2nd Combat Program
import random
import time

health_roll = random.randint(1, 20)
defense_roll = random.randint(1, 15)
attack_roll = random.randint(1, 10)

fighters = { #change numbers idk what im doing, may have to change this into variables based on logic
    "Knight":{
        "option_num" : 1,
        "health" : 8 + health_roll,
        "defense" : 6 + defense_roll,
        "attack" : 5 + attack_roll,
    },
    "Mage":{
        "option_num" : 2,
        "health" : 5 + health_roll,
        "defense" : 8 + defense_roll,
        "attack" : 10 + attack_roll,
    },
    "Rogue":{
        "option_num" : 3,
        "health" : 4 + health_roll,
        "defense" : 5 + defense_roll,
        "attack" : 13 + attack_roll,
    }
}

enemies = {
    "Ogre":{
        "health" : 40,
        "defense" : 8,
        "attack" : 12,
    },
    "Slime":{
        "health" : 20,
        "defense" : 5,
        "attack" : 8,
    },
    "Wolf":{
        "health" : 30,
        "defense" : 10,
        "attack" : 10,
    },
}

def user_combat():
    print("Action time!")
    print("1. Normal Attack \n2. Wild Attack(you take a little bit of damage) \n3. Heal(by 6 points) \n4. Guard(raise your defense by 3)")
    user_action = input("What would you like to do?: ")
    if user_action == "1":
        damage = user_fighter["attack"] - enemy_fighter["defense"]
        enemy_fighter["health"] -= damage
        print(f"You did a normal attack. {enemy_choice} now has {enemy_fighter["health"]} health left.")
    elif user_action == "2":
        print("You did a wild attack.")
    elif user_action == "3":
        print("You healed yourself.")
    elif user_action == "4":
        print("You guarded yourself for one turn.")

print("Hello! This a combat training simulator.")
name = input("First off, what is your name?: ")
print(f"Nice to meet you, {name}! \nNow, here are your options for the classes: \n1 for a Knight \n2 for a Mage \n3 for a Rogue.")
user_fighter = input("Choose a class: ")
print("Awesome! Now...\n")

if user_fighter == "1":
    user_fighter = fighters["Knight"]
    print(f"You are a Knight. \nYour stats are: \nHealth: {fighters["Knight"]["health"]} \nDefense: {fighters["Knight"]["defense"]} \nAttack: {fighters["Knight"]["attack"]}")
elif user_fighter == "2":
    user_fighter = fighters["Mage"]
    print(f"You are a Mage. \nYour stats are: \nHealth: {fighters["Mage"]["health"]} \nDefense: {fighters["Mage"]["defense"]} \nAttack: {fighters["Mage"]["attack"]}")
elif user_fighter == "3":
    user_fighter = fighters["Rogue"]
    print(f"You are a Rogue. \nYour stats are: \nHealth: {fighters["Rogue"]["health"]} \nDefense: {fighters["Rogue"]["defense"]} \nAttack: {fighters["Rogue"]["attack"]}")

enemy_choice = random.choice(list(enemies.keys()))
if enemy_choice == "Ogre":
    enemy_fighter = enemies["Ogre"]
elif enemy_choice == "Slime":
    enemy_fighter = enemies["Slime"]
elif enemy_choice == "Wolf":
    enemy_fighter = enemies["Wolf"]

time.sleep(1)
print(f"\nA wild {enemy_choice} has appeared!")
user_combat()

