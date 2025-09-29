#VY 2nd Shopping Lits Manager

while True:
    action = input("What would you like to do?(view, add, remove, exit): ")
    #Write your code here
    if action.strip().lower() == "view":
        print("yum")
    elif action.strip().lower() == "add":
        print("wonderhoy")
    elif action.strip().lower() == "remove":
        print("oyasumi")
    elif action == "exit":
        print("k bye")
        break
    else:
        print("what did you just put")