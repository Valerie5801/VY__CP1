#VY 2nd Final Project
import random

user_location = 1
spirit_locations = [3, 6, 4]
boss_location = 9
extra_entity = {}
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

game_items = {
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
        "Property": "Attack",
        "Effect": 10,
        "Inventory": False,
        "Room": 6
    },
    "Shield": {
        "Use": "Equip",
        "Property": "Defense",
        "Effect": 10,
        "Inventory": False,
        "Room": 4
    }
}

back_usr_location = user_location
back_usr_stats = user_stats
back_spirit_stats = spirit_stats
back_boss_stats = boss_stats
back_items = game_items

#Combat functions
def user_combat(enemy_stats):
    print("Your turn.")
    if enemy_stats["Type"] == "Spirit":
        print("1. Attack \n2. Flee \n 3. Expel \n4. Guard")
    elif enemy_stats["Type"] == "Warden":
        print("1. Attack \n2. Flee \n 3. Charged Attack \n4. Guard")
    
    while True:
        user_action = input("What would you like to do?(1/2/3/4): ")

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
    if going_first == 1 and enemy["Type"] == "Spirit":
        print("You are going first.")
        user_stats, enemy_spirit = user_combat(spirit_stats)
        turn = "enemy"
    elif going_first == 1 and enemy["Type"] == "Warden":
        print("You are going first.")
        user_stats, boss_stats = user_combat(boss_stats)
        turn = "enemy"
    elif going_first == 2 and enemy["Type"] == "Spirit":
        print(f"{enemy["Type"]} is going first.")
        user_stats, enemy_spirit = spirit_combat(spirit_stats)
        turn = "player"
    elif going_first == 2 and enemy["Type"] == "Warden":
        print(f"{enemy["Type"]} is going first.")
        user_stats, boss_stats = boss_combat()
        turn = "player"
    if going_first == 2 and enemy["Type"] == "Spirit":
        while True:
            if turn == "enemy":
                print(f"{enemy["Type"]}'s turn.")
                user_stats, enemy_spirit = spirit_combat(enemy_spirit)
                turn = "player"
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                elif enemy_spirit["Health"] == 0:
                    print("You win!")
                    break
                else:
                    continue
            elif turn == "player":
                print(f"{enemy["Type"]}'s turn.")
                user_stats, enemy_spirit = user_combat(enemy_spirit)
                turn = "enemy"
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                elif enemy_spirit["Health"] == 0:
                    print("You win!")
                    break
                else:
                    continue
    if going_first == 1 and enemy["Type"] == "Warden":
        while True:
            if turn == "enemy":
                print(f"{enemy["Type"]}'s turn.")
                user_stats, boss_stats = boss_combat()
                turn = "player"
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                elif boss_stats["Health"] == 0:
                    print("You win!")
                    break
                else:
                    continue
            elif turn == "player":
                print(f"{enemy["Type"]}'s turn.")
                user_stats, boss_stats = user_combat(boss_stats)
                turn = "enemy"
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                elif boss_stats["Health"] == 0:
                    print("You win!")
                    break
                else:
                    continue
    return user_stats, enemy


def movement():
    if user_location == 1:
        print("You can go to rooms 4 or 2.")
    elif user_location == 2:
        print("You can go to rooms 4, 1, or 6.")
    elif user_location == 3:
        print("You can go to rooms 5, 7, or 8.")
    elif user_location == 4:
        print("You can go to rooms 1, 2, or 7.")
    elif user_location == 5:
        print("You can go to rooms 3, 7, 8, or 6.")
    elif user_location == 6:
        print("You can go to rooms 2, 5, or 8.")
    elif user_location == 7:
        print("You can go to rooms 4, 5, or 3.")
    elif user_location == 8:
        print("You can go to rooms 5, 3, 6, or 9.")
    next_room = input("What location would you like to go to?(as a number): ")
    print(f"You make you way over to room {next_room}.")
    return next_room


def inventory():
    user_equip = input("Do you want to equip/use an item or unequip an item?(e/u, n if you want to back out): ")
    if user_equip == "n":
        is_inventory = []
        for exist_item in game_items.keys():
            if exist_item["Inventory"]:
                is_inventory.append(exist_item)
        print("Here are the items in your inventory:")
        for item in is_inventory:
            print(item)
        if user_equip.lower() == "e":
            while True:
                item_used = input('What item do you want to use/equip?(to back out, type "no"): ')
                if item_used not in is_inventory:
                    print("That isn't in your inventory. Please try again.")
                    continue
                elif item_used.lower() == "no":
                    break
                for exist_item in game_items.keys():
                    if item_used == exist_item:
                        for stat in user_stats.keys():
                            if stat == exist_item["Property"]:
                                exist_item["Effect"] += user_stats[stat]
            print(f"You used {item_used}. Your {stat} stat is now {user_stats[stat]}")
        elif user_equip.lower() == "u":
            while True:
                item_unequip = input("What item do you want to unequip?(dagger or shield, no to back out): ")
                if item_unequip.capitalize() not in is_inventory:
                    print("It currently isn't in your inventory.")
                elif item_unequip == "no":
                    break
                for exist_item in game_items.keys():
                    if item_unequip == exist_item and exist_item["Use"] == "Equip":
                        for stat in user_stats.keys():
                            if stat == exist_item["Property"]:
                                exist_item["Effect"] -= user_stats[stat]
            print(f"You unequipped {item_unequip}. Your {stat} stat is now {user_stats[stat]}")
    return user_stats, game_items


def explore():
    for exist_item in game_items.keys():
        if game_items[exist_item] == user_location:
            print(f"{game_items[exist_item]} is in the room.")
            user_take = input("Do you want to take it?(y/n): ")
            if user_take == "y":
                while True:
                    get_item = input("What item do you want to take?: ")
                    if get_item.capitalize() != game_items[exist_item]:
                        print("That item isn't in the room.")
                    else: 
                        for game_item in game_items.keys():
                            if game_items[game_item] == get_item:
                                game_items[game_item]["Inventory"] == True
                                print(f"You took the {exist_item}")
            elif user_take == "n":
                print("You decide to leave it.")
    return game_items


def menu():
    new_location = ""
    new_inventory = ""
    print("You can go to another room (1), check your inventory (2), or explore this room (3).")
    user_choice = input("What do you want to do?(1/2/3): ")
    if user_choice == "1":
        new_location = int(movement())
        new_inventory = game_items
    elif user_choice == "2":
        new_inventory = inventory()
        new_location = user_location
    elif user_choice == "3":
        new_inventory = explore()
        new_location = user_location
    return new_location, new_inventory

def restart():
    user_restart = input("Would you like to restart the game?(y/n): ")
    if user_restart == "y":
        user_restart = True
        user_location = back_usr_location
        user_stats = back_usr_stats
        spirit_stats = back_spirit_stats
        boss_stats = back_boss_stats
        game_items = back_items
    elif user_restart == "n":
        user_restart = False
    return user_restart


while True:
    print("You find yourself in an old looking dungeon. How did you get here? Why are you here?")
    print("You need to fight your way out in order to escape. Let's start.")
    while True:
        if user_stats["Health"] == 0:
            print("You have lost.")
            another_game = restart()
            if not another_game:
                print("Thank you for playing.")
            break
        elif boss_stats["Health"] == 0:
            print("You managed to beat the master and escape.")
            if not another_game:
                print("Thank you for playing.")
            break
        if user_location == boss_location:
            fight = input("Do you want to face the master?(y/n): ")
            user_stats, boss_stats = main_battle(boss_stats)
        elif user_location in spirit_locations:
            user_stats, extra_entity = main_battle(spirit_stats)
        extra_entity = {}
        user_location, game_items = menu()
    if another_game:
        break
        