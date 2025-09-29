#VY 2nd Lists Notes

import random

names = ["Omori", "Sunny", "Aubrey", "Kel", "Hero", "Basil", "Mari"]

print(names)
print(names[4])

print(names[random.randint(1,len(names))])
print(random.choice(names))

names[-1] = "Something"
names.extend(["Stranger", "Mewo"])

print(names)

names.remove("Omori")
specific = names.index("Stranger")
names.pop(specific)
print(names)

print(specific)

#For tic tac toe
board = [[1,2,3],
         [4,5,6],
         [7,8,9]]

board[1][1] = "X"
print(board)

#Tuple
classes = ("Bard", "Monk", "Barbarian", "Paladin")

#Set
fruit = {"apple", "orange", "banana"}