#VY 2nd Final Project
import random

user_location = 1
spirit_locations = [3, 6, 4]
boss_location = 9

user_stats = {
    "Health": 50,
    "Attack": 5,
    "Defense": 2,
    "Guard": False,
    "Charge counter": 0
}

spirit_stats = {
    "Type": "Spirit",
    "Health": 30,
    "Attack": 4,
    "Defense": 1
}

boss_stats = {
    "Type": "Warden",
    "Health": 70,
    "Attack": 4,
    "Defense": 4,
    "Charge counter": 0
}

items = {
    "Bandage": {
        "Use": 1,
        "Property": "Health",
        "Effect": 10,
        "Inventory": False,
        "Room": 7
    },
    "Healing Potion": {
        "Use": 1,
        "Property": "Health",
        "Effect": 25,
        "Inventory": False,
        "Room": 2
    },
    "Defense Potion": {
        "Use": 1,
        "Property": "Defense",
        "Effect": 2,
        "Inventory": False,
        "Room": 5
    },
    "Attack Potion": {
        "Use": 1,
        "Property": "Attack",
        "Effect": 10,
        "Inventory": False,
        "Room": 2
    },
    "Dagger": {
        "Use": "Equip",
        "Property": "Health",
        "Effect": 10,
        "Inventory": False,
        "Room": 7
    },
    "Bandage": {
        "Use": 1,
        "Property": "Health",
        "Effect": 10,
        "Inventory": False,
        "Room": 7
    }
}

#Combat functions
def user_combat(enemy_stats):
    print("Your turn.")
    if enemy_stats["Type"] == "Spirit":
        print("1. Attack \n2. Flee \n 3. Expel \n4. Guard")
    elif enemy_stats["Type"] == "Warden":
        print("1. Attack \n2. Flee \n 3. Charged Attack \n4. Guard")
    
    while True:
        user_action = input("What would you like to do?: ")

        if user_action == "1":
            damage = user_stats["Attack"] - enemy_stats["Defense"]
            enemy_stats["Health"] -= damage
            if enemy_stats["Health"] < 0:
                enemy_stats["Health"] == 0
            print(f"You attacked. {enemy_stats["Type"]} took {damage} damage. It now has {enemy_stats["Health"]} health left.")
            break
        elif user_action == "2":
            flee_chance = random.randint(1, 10)
            if flee_chance <= 3: #add a way for the user to back out of the final boss battle and return them to the previous room.
                enemy_stats["Health"] = -1
                print("You successfully ran away.")
            else:
                print("You failed to run away.")
            break
        elif user_action == "3":
            if enemy_stats["Type"] == "Spirit":
                print("You try to erase the spirit from existence.")
                expel_chance = random.randint(1, 10)
                if expel_chance == 5:
                    enemy_stats["Health"] = 0
                    print("You expelled the spirit.")
                else:
                    print("You failed to expel the spirit.")
                break
            elif enemy_stats["Type"] == "Warden" and user_stats["Charge counter"] <= 3:
                damage = (user_stats["Attack"] + 4) - enemy_stats["Defense"]
                enemy_stats["Health"] -= damage
                print(f"You do a charged attack. Warden has {enemy_stats["Health"]} health left.")
                user_stats["Charge counter"] += 1
                break
            else:
                print("You cannot do any more charge attacks.")
        elif user_action == "4":
            user_stats["Guard"] = True
            print("You guarded yourself.")
            break

    return user_stats, enemy_stats


def spirit_combat(enemy_stats):
    print("Spirit's turn.")
    damage = enemy_stats["Attack"] - user_stats["Defense"]
    if user_stats["Guard"]:
        damage -= 2
        user_stats["Guard"] = False

    user_stats["Health"] -= damage
    if user_stats["Health"] < 0:
        user_stats["Health"] = 0
    
    print(f"Spirit attacks you for {damage} damage. You now have {user_stats["Health"]} health left.")
    return user_stats, enemy_stats


def boss_combat():
    print("Warden's turn.")
    boss_action = random.randint(1, 2)
    if boss_stats["Charge counter"] <= 2:
        boss_action = 1
    
    if boss_action == 1:
        print("Warden does a normal attack.")
        damage = boss_stats["Attack"] - user_stats["Defense"]
        if user_stats["Guard"]:
            damage -= 2
            user_stats["Guard"] = False
    elif boss_action == 2:
        print("Warden does a charged attack.")
        damage = boss_stats["Attack"]
        if user_stats["Guard"]:
            damage -= 2
            user_stats["Guard"] = False
        boss_stats["Charge counter"] += 1

    user_stats["Health"] -= damage
    print(f"Warden did {damage} damage. You now have {user_stats["Health"]} health left.")
    return user_stats, boss_stats


def main_battle(enemy):
    print(f"{enemy["Type"]} appeared!")
    going_first = random.randint(1, 2)
    