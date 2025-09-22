#VY 2nd User Sign in

users = [["OMORI", "somethingisbehindyou"], ["Aubrey", "itmeanteverything"], ["Kel", "threedaysleft"]]

while True:
    name_input = input("What is your username?: ")
    pass_check = input("What is your password?: ")
    if name_input in users[0][0] or name_input in users[1][0] or name_input in users[2][0]:
        if pass_check in users[0][1] or pass_check in users[1][1] or pass_check in users[2][1]:
            print("Welcome back!")
            break
        else:
            print("Your password is wrong")
            break
    else:
        print("I don't recognize your username.")
        break


#username = "OMORI" #setting username and password
#password = "somethingisbehindyou"

#name_input = input("What is your username?: ")
#if name_input == username: #checking for username
 #   pass_input = input("What is your password?:")
  #  if pass_input == password: #if the username is the same, checking for password
   #     print(f"Welcome back, {username}")
   # else:
    #    print("You were wrong. Go back")
#else:
 #   print("I dont recognize that username.")