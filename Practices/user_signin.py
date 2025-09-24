#VY 2nd User Sign in

users = [["OMORI", "somethingisbehindyou"], ["Aubrey", "itmeanteverything"], ["Kel", "threedaysleft"]]

while True:
    name_input = input("What is your username?: ")
    pass_check = input("What is your password?: ")
    user_found = False
    for user, password in users:
        if name_input == user and pass_check == password:
            print("Welcome back!")
            user_found = True
            break
        elif name_input == user and pass_check != password:
            print("Password is incorrect.")
            break
        elif name_input != user:
            print("Username doesn't exist.")
            break
        else:
            continue
    if not user_found:
        print("Something is wrong.")
    break