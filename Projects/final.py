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
    "Charge_counter": 0
}

spirit_stats = {
    "Type": "Spirit",
    "Health": 30,
    "Attack": 4,
    "Defense": 1
}

boss_stats = {
    "Type": "Boss",
    "Health": 70,
    "Attack": 4,
    "Defense": 4,
    "Charge_counter": 0
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