#VY 2nd Who Are You

name = input("What is your name?: ")
userAge = input("How old are you?: ")
color = input("What's your favorite color?: ")
nameList = [name]

print("So, ", name, ", you're ", userAge, "years old, and you like the color", color, "? It's nice to meet you!")

newName = input("What is your name?: ")
if newName in name:
     name = newName
     print("hi")
else:
     print("i think youre new")