#VY 2nd Conditionals Notes

import random
monster_hp = 30 #setting variables
dmg_modifier = 2
atk_bonus = 3
player_hp = 25

roll = random.randint(1, 20) #dice

if roll == 20: #checking for critical hit
    print("wow you got a crit now double your damage")
    attack = random.randint(1, 8) + random.randint(1, 8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster")

elif roll+atk_bonus > 10: #checking if the player actually hits
    print(f"you hit them")
    attack = random.randint(1, 8) + dmg_modifier
    monster_hp -= attack
    print(f"You did {attack} damage to the monster")

elif roll <= 10: #checking if the player's luck is bad
    if roll == 1: #checking if the player's luck is absolutely horrendous
        print("your luck is terrible its so bad that the monster can attack you when it shouldn't")
        damage = random.randint(1, 10) + 2
        player_hp -= damage
        print(f"you took {damage} damage so now you have {player_hp} hp")
    else:
        print("sad you missed")
        
else: #fail-safe incase the player is so stupid they get a different value or if the player is so smart they get a different value
    print("what the heck did you get")

print("turn is over")