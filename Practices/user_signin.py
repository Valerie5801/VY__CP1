#VY 2nd User Sign in

username = "OMORI" #setting username and password
password = "somethingisbehindyou"

name_input = input("What is your username?: ") #getting user inputs
pass_input = input("What is your password?:")

if username == "OMORI": #checking for username
    if password == "somethingisbehindyou": #if the username is the same, checking for password
        print(f"Welcome back, {username}")
    else:
        print("You were wrong. Go back")
else:
    print("I dont recognize that username.")