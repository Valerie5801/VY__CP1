# VY 2nd Hello World First Practice
existingUser = ["Sunny", "Aubrey", "Kel", "Hero", "Basil"]
admin = ["Valerie", "Ms. LaRose"]
name = input("What's your name?: ")

if name in admin:
    print("Greetings, admin.")
elif name in existingUser:
    print("Welcome back!")
else:
    print("Welcome new user!")