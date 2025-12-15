#VY 2nd Final Project
import random #Warden fight and warden charged attacks are bugged.
import time

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
        "Room": 1
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
        "Room": 4
    },
    "Dagger": {
        "Use": "Equip",
        "Property": "Attack",
        "Effect": 10,
        "Inventory": False,
        "Equipped": False,
        "Room": 6
    },
    "Shield": {
        "Use": "Equip",
        "Property": "Defense",
        "Effect": 10,
        "Inventory": False,
        "Equipped": False,
        "Room": 6
    }
}

game_map = {
    "Connected One": [4, 2],
    "Connected Two": [4, 1, 6],
    "Connected Three": [5, 7, 8],
    "Connected Four": [1, 2, 7],
    "Connected Five": [3, 7, 8, 6],
    "Connected Six": [2, 5, 8],
    "Connected Seven": [4, 5, 3],
    "Connected Eight": [5, 3, 6, 9],
}

notes = {
    1: "\nI've been here for ages. I can't decide if I should leave or not. I'm scared of whatever is out there.\n",
    4: "\nI'm going in circles. Can't tell if anyone is reading this, but if so, best of luck to you.\n",
    6: "\nHow old is this place, like seriously? It's really worn-down. Why does the warden still stay in this place?\n",
    8: "\nMy pen is dying, so I guess I can't write anymore...that sucks.\n"
}

back_usr_location = user_location
back_usr_stats = user_stats
back_spirit_stats = spirit_stats
back_boss_stats = boss_stats
back_items = game_items
another_game = True  #restart flag
past_location = 1

#Combat functions
def user_combat(enemy_stats):
    print("Your turn.")
    if enemy_stats["Type"] == "Spirit":
        print("1. Attack \n2. Flee \n3. Expel \n4. Guard \n")
    elif enemy_stats["Type"] == "Warden":
        print("1. Attack \n2. Flee \n3. Charged Attack \n4. Guard \n")
    time.sleep(1)
    while True:
        user_action = input("What would you like to do?(1/2/3/4): ")

        if user_action == "1":
            damage = user_stats["Attack"] - enemy_stats["Defense"]
            enemy_stats["Health"] -= damage
            if enemy_stats["Health"] < 0:
                enemy_stats["Health"] = 0
            print(f"You attacked. {enemy_stats['Type']} took {damage} damage. It now has {enemy_stats['Health']} health left.")
            break
        elif user_action == "2":
            flee_chance = random.randint(1, 10)
            if flee_chance <= 3:
                enemy_stats["Health"] = 0
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
                print(f"You do a charged attack. Warden has {enemy_stats['Health']} health left.")
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
    damage = enemy_stats["Attack"] - user_stats["Defense"]
    if user_stats["Guard"]:
        damage -= 2
        user_stats["Guard"] = False

    user_stats["Health"] -= damage
    if user_stats["Health"] < 0:
        user_stats["Health"] = 0
    
    print(f"Spirit attacks you for {damage} damage. You now have {user_stats['Health']} health left.")
    time.sleep(1)
    return user_stats, enemy_stats


def boss_combat(enemy_stats):
    boss_action = random.randint(1, 2)
    if enemy_stats["Charge counter"] <= 2:
        boss_action = 1
    
    if boss_action == 1:
        print("Warden does a normal attack.")
        time.sleep(0.5)
        damage = enemy_stats["Attack"] - user_stats["Defense"]
        if user_stats["Guard"]:
            damage -= 2
            user_stats["Guard"] = False
    elif boss_action == 2:
        print("Warden does a charged attack.")
        time.sleep(0.5)
        damage = enemy_stats["Attack"]
        if user_stats["Guard"]:
            damage -= 2
            user_stats["Guard"] = False
        enemy_stats["Charge counter"] += 1

    user_stats["Health"] -= damage
    print(f"Warden did {damage} damage. You now have {user_stats['Health']} health left.")
    return user_stats, enemy_stats


def main_battle(enemy):
    enemy_spirit = spirit_stats
    enemy_boss = boss_stats
    print(f"{enemy['Type']} appeared!\n")
    going_first = random.randint(1, 2)
    if going_first == 1 and enemy["Type"] == "Spirit":
        print("You are going first.")
        time.sleep(1)
        user_stats, enemy_spirit = user_combat(enemy_spirit)
        turn = "enemy"
    elif going_first == 1 and enemy["Type"] == "Warden":
        print("You are going first.")
        time.sleep(1)
        user_stats, enemy_boss = user_combat(enemy_boss)
        turn = "enemy"
    elif going_first == 2 and enemy["Type"] == "Spirit":
        print(f"{enemy['Type']} is going first.")
        time.sleep(1)
        user_stats, enemy_spirit = spirit_combat(enemy_spirit)
        turn = "player"
    elif going_first == 2 and enemy["Type"] == "Warden":
        print(f"{enemy['Type']} is going first.")
        time.sleep(1)
        user_stats, enemy_boss = boss_combat(enemy_boss)
        turn = "player"
    
    if going_first == 1:
        while True:
            if turn == "player":
                if enemy["Type"] == "Spirit":
                    user_stats, enemy_spirit = user_combat(enemy_spirit)
                else:
                    user_stats, enemy_boss = user_combat(enemy_boss)
                
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                if enemy_spirit["Health"] == 0 or enemy_boss["Health"] == 0:
                    print("You win!")
                    break
                turn = "enemy"

            elif turn == "enemy":
                print(f"{enemy['Type']}'s turn.")
                time.sleep(1)
                if enemy["Type"] == "Spirit":
                    user_stats, enemy_spirit = spirit_combat(enemy_spirit)
                else:
                    user_stats, enemy_boss = boss_combat(enemy_boss)

                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                if enemy_spirit["Health"] == 0 or enemy_boss["Health"] == 0:
                    print("You win!")
                    break
                turn = "player"

    elif going_first == 2:
        while True:
            if turn == "player":
                if enemy["Type"] == "Spirit":
                    user_stats, enemy_spirit = user_combat(enemy_spirit)
                else:
                    user_stats, enemy_boss = user_combat(enemy_boss)
                
                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                if enemy_spirit["Health"] == 0 or enemy_boss["Health"] == 0:
                    print("You win!")
                    break
                turn = "enemy"

            elif turn == "enemy":
                print(f"{enemy['Type']}'s turn.")
                time.sleep(1)
                if enemy["Type"] == "Spirit":
                    user_stats, enemy_spirit = spirit_combat(enemy_spirit)
                else:
                    user_stats, enemy_boss = boss_combat(enemy_boss)

                if user_stats["Health"] == 0:
                    print("You lose.")
                    break
                if enemy_spirit["Health"] == 0 or enemy_boss["Health"] == 0:
                    print("You win!")
                    break
                turn = "player"

    return user_stats, enemy


def movement():
    room_connections = {
        1: ("4 or 2", "Connected One"),
        2: ("4, 1, or 6", "Connected Two"),
        3: ("5, 7, or 8", "Connected Three"),
        4: ("1, 2, or 7", "Connected Four"),
        5: ("3, 7, 8, or 6", "Connected Five"),
        6: ("2, 5, or 8", "Connected Six"),
        7: ("4, 5, or 3", "Connected Seven"),
        8: ("5, 3, 6, or 9", "Connected Eight")
    }
    
    while True:
        available_rooms, map_key = room_connections[user_location]
        print(f"You can go to rooms {available_rooms}.")
        
        next_room = input("What location would you like to go to?(as a number): ")
        if not next_room.isnumeric():
            print("That isn't a number. Please enter a valid room number.")
            continue
        
        next_room = int(next_room)
        if next_room not in game_map[map_key]:
            print("You can't go there...")
            continue
        
        break
    
    print(f"You make you way over to room {next_room}.\n")
    return next_room


def inventory(existing_items):
    is_inventory = []
    for exist_item in existing_items.keys():
        if existing_items[exist_item]["Inventory"]:
            is_inventory.append(exist_item)
    
    if not is_inventory:
        print("There is nothing in your inventory.")
        return existing_items, user_stats
    
    print("Here are the items in your inventory:")
    for item in is_inventory:
        print(f"\t-{item}")
    
    user_equip = input("Do you want to equip/use an item or unequip an item?(e/u, n if you want to back out): ")
    
    if user_equip.lower() == "e":
        while True:
            item_used = input('What item do you want to use/equip?(to back out, type "no"): ')
            if item_used.lower() == "no":
                break
            if item_used not in is_inventory:
                print("That isn't in your inventory. Please try again.")
                continue
            for exist_item in existing_items.keys():
                if item_used.lower() == exist_item.lower():
                    prop = existing_items[exist_item]["Property"]
                    effect = existing_items[exist_item]["Effect"]
                    use_type = existing_items[exist_item]["Use"]
                    if use_type == "Equip": #equippable
                        if existing_items[exist_item].get("Equipped", False):
                            print(f"{item_used} is already equipped.")
                        else:
                            user_stats[prop] += effect
                            existing_items[exist_item]["Equipped"] = True
                            print(f"You equipped {item_used}. Your {prop} stat is now {user_stats[prop]}")
                    else: #one-time use
                        user_stats[prop] += effect
                        existing_items[exist_item]["Inventory"] = False
                        print(f"You used {item_used}. Your {prop} stat is now {user_stats[prop]}")
                    break
            break
    elif user_equip.lower() == "u":
        while True:
            item_unequip = input("What item do you want to unequip?(to back out, type 'no'): ")
            if item_unequip.lower() == "no":
                break
            if item_unequip not in is_inventory:
                print("It currently isn't in your inventory.")
                continue
            # Find and unequip the item
            for exist_item in existing_items.keys():
                if item_unequip.lower() == exist_item.lower() and existing_items[exist_item]["Use"] == "Equip":
                    if not existing_items[exist_item].get("Equipped", False):
                        print(f"{item_unequip} is not currently equipped.")
                    else:
                        prop = existing_items[exist_item]["Property"]
                        effect = existing_items[exist_item]["Effect"]
                        user_stats[prop] -= effect
                        existing_items[exist_item]["Equipped"] = False
                        print(f"You unequipped {item_unequip}. Your {prop} stat is now {user_stats[prop]}")
                    break
            break
    elif user_equip.lower() == "n":
        print("You decide to not use anything.\n")
    
    return existing_items, user_stats


def explore(existing_items):
    item_in_room = False
    for exist_item in existing_items.keys():
        if existing_items[exist_item]["Room"] == user_location and existing_items[exist_item]["Inventory"] == False:
            print(f"{exist_item} is in the room.")
            item_in_room = True
            user_take = input("Do you want to take it?(y/n): ")
            if user_take == "y":
                existing_items[exist_item]["Inventory"] = True
                print(f"You took the {exist_item}\n")
            elif user_take == "n":
                print("You decide to leave it.\n")
    for note in notes.keys():
        if note == user_location:
            item_in_room = True
            print("There is a note here.")
            if user_location == 1:
                print("It looks very tattered and old...")
            print(notes[note])
    if not item_in_room:
       print("There is nothing in this room.\n")
    return existing_items


def menu(): #needs to be idiot-proofed
    new_location = user_location
    new_inventory = game_items
    new_stats = user_stats
    while True:
        print("You can go to another room (1), check your inventory (2), or explore this room (3).")
        user_choice = input("What do you want to do?(1/2/3): ").strip().lower()
        if user_choice == "1":
            new_location = int(movement())
            new_inventory = game_items
            new_stats = user_stats
            break
        elif user_choice == "2":
            new_inventory, new_stats = inventory(game_items)
            new_location = user_location
            break
        elif user_choice == "3":
            new_inventory = explore(game_items)
            new_location = user_location
            new_stats = user_stats
            break
        else:
            print("That isn't a valid option. Please try again.\n")
            continue
    return new_location, new_inventory, new_stats

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
    time.sleep(1)
    while True:
        if user_location == 8 or user_location == 6:
            past_location = user_location
        if user_stats["Health"] == 0:
            print("You have lost.")
            another_game = restart()
            if another_game:
                break
            else:
                print("Thank you for playing.")
                break
        elif boss_stats["Health"] == 0:
            print("You managed to beat the master and escape.")
            another_game = restart()
            if another_game:
                break
            else:
                print("Thank you for playing.")
                break
        if user_location == boss_location:
            fight_master = input("Do you want to face the warden?(y/n): ")
            if fight_master == "y":
                user_stats, boss_stats = main_battle(boss_stats)
                continue
            else:
                print("You decide to turn back.")
                user_location = past_location
                continue
        elif user_location in spirit_locations:
            user_stats, extra_entity = main_battle(spirit_stats)
            spirit_locations.remove(user_location)
            continue
        extra_entity = {}
        user_location, game_items, user_stats = menu()
    if not another_game:
        break
    break
