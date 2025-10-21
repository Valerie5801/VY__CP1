#VY 2nd Functions Notes
#all imports
num = 0 #Global variables
player_hp = 100
monster_hp = 100

#functions
def add(x, y):
    return x+y

def initials(name):
    names = name.split(" ")
    initial = ""
    for name in names:
        initial += name[0]
    return initial

def attack(dmg, turn):
    if turn == "player":
        return monster_hp - dmg, player_hp
    else:
        return monster_hp, player_hp - dmg


#rest of the code
while num < add(1, 3):
    print("wonder")
    num+=1
print("hoy")
print(f"Your number is: {add(5, 3)}")
total = add(8, 13) #setting functions as a variable
print(add(add(3, 2), 10)) #using the result of a function as another function's parameter
add(32429865743985,98547285)

print(f"Tia's initials are: {initials("Tia LaRose")}")

monster_hp, player_hp = attack(15, "player")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

monster_hp, player_hp = attack(15, "monster")
print(f"Player Health: {player_hp}")
print(f"Monster Health: {monster_hp}")

#ASCII
print(f"a = {ord("a")}")
print(f"100 = {chr(100)}")