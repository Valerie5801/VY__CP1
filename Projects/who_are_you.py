#VY 2nd Who Are You

allInfo = {}
userInfo = {}


while True:
     name = input("What is your name?(type 'quit' to stop): ")
     if name.lower() == 'quit': #terminating the program
          print("Goodbye.")
          break
     elif name in userInfo: #recognizing a name
          recognizedInfo = userInfo[name]
          print(f"Welcome back, {name}! You were {recognizedInfo['age']} years old and your favorite color was {recognizedInfo['color']} last time.")
     else: #saving a new user's information
          userAge = input(f"How old are you, {name}?: ")
          color = input("What's your favorite color?: ")

          userInfo[name] = {"age":userAge, "color":color}
          allInfo["user"] = userInfo

          print("So, ", name, ", you're ", userAge, "years old, and you like the color", color, "? It's nice to meet you!")