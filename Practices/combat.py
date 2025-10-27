#VY 2nd Combat Program
import random
import time

fighters = {
    "Knight":{
        "option_num" : 1,
        "health" : 30,
        "defense" : 4,
        "attack" : 5 ,
    },
    "Mage":{
        "option_num" : 2,
        "health" : 25,
        "defense" : 4,
        "attack" : 4,
    },
    "Rogue":{
        "option_num" : 3,
        "health" : 15,
        "defense" : 3,
        "attack" : 6,
    }
}

enemies = {
    "Ogre":{
        "health" : 35,
        "defense" : 3,
        "attack" : 5,
    },
    "Slime":{
        "health" : 15,
        "defense" : 3,
        "attack" : 3,
    },
    "Wolf":{
        "health" : 25,
        "defense" : 5,
        "attack" : 4,
    },
}

def user_combat():
    print("Your turn.")
    print("1. Normal Attack \n2. Wild Attack(you take a little bit of damage) \n3. Heal(by 6 points) \n4. Skip.")
    user_action = input("What would you like to do?: ")
    if user_action == "1":
        damage = user_fighter["attack"] - enemy_fighter["defense"]
        enemy_fighter["health"] -= damage
        if enemy_fighter["health"] < 0:
            enemy_fighter["health"] == 0
        print(f"You did a normal attack. {enemy_choice} now has {enemy_fighter["health"]} health.\n")
        time.sleep(1.5)
    elif user_action == "2":
        recoil = random.randint(2, 3)
        enemy_fighter["health"] -= user_fighter["attack"]
        user_fighter["health"] -= recoil
        if user_fighter["health"] < 0:
            user_fighter["health"] == 0
        if enemy_fighter["health"] < 0:
            enemy_fighter["health"] == 0
        print(f"You did a wild attack. {enemy_choice} now has {enemy_fighter["health"]} health. \nHowever, you took {recoil} damage. You now have {user_fighter["health"]} health.\n")
        time.sleep(1.5)
    elif user_action == "3":
        user_fighter["health"] += 6
        print(f"You healed yourself by 6 points. You now have {user_fighter["health"]} points of health left.\n")
        time.sleep(1.5)
    elif user_action == "4":
        print("You skipped your turn.\n")
        time.sleep(1.5)
    return user_fighter, enemy_fighter

def enemy_combat():
    print(f"{enemy_choice}'s turn.")
    damage = enemy_fighter["attack"] - user_fighter["defense"]
    user_fighter["health"] -= damage
    if user_fighter["health"] < 0:
        user_fighter["health"] == 0
    print(f"{enemy_choice} attacks you. \nYou now have {user_fighter["health"]} health.\n")
    time.sleep(1.5)
    return user_fighter

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

time.sleep(1.5)
print(f"\nA wild {enemy_choice} has appeared!")

first = random.randint(1, 2)
if first == 1:
    print("You get to go first.")
    user_combat()
    turn = "enemy"
elif first == 2:
    print(f"{enemy_choice} is going first.")
    enemy_combat()
    turn = "player"

while True:
    if turn == "enemy":
        enemy_combat()
        turn = "player"
        if user_fighter["health"] == 0:
            print("You lost.")
            break
        elif enemy_fighter["health"] == 0:
            print("You won!")
            break
        else:
            continue
    elif turn == "player":
        user_combat()
        turn = "enemy"
        if user_fighter["health"] == 0:
            print("You lost.")
            break
        elif enemy_fighter["health"] == 0:
            print("You won!")
            break
        else:
            continue