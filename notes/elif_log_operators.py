#VY 2nd Elif and Logical Operators notes

homework = True
chores = True
room = True

if homework and chores and room:
    print("ok free time")
elif not chores or not room:
    print("do chores and clean your room")
else:
    print("no finish homeworks first")


username = input("Enter username here: ")
password = input("Enter password here: ")

if username == "Mari" and password == "dearlittlebrother": #You can have as many elifs as you want
    print("Hello, Mari.")
elif username == "OMORI" and password == "youlovedherandyoulefther":
    print("Welcome to White Space. You have been living here for as long as you remember.")
elif username == "Basil" and password == "somethingisbehindyou":
    print("Everything will be okay...")
elif username == "Aubrey" and password == "itmeanteverything":
    print("They are still your friends.")
elif username == "Kel" and password == "threedaysleft":
    print("Did he open the door?")
elif username == "Hero" or username == "Henry" and password == "sheisgone":
    print("Things will get better.")
elif username == "Sunny":
    if password == "goodmorningorgoodnight": #nested if statement
        print("You are moving in three days after four years of staying in your house.")
    else:
        print("Incorrect Password")
else:
    print("No.")