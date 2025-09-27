#VY 2nd Fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #guess = input("Enter your guess: ")
        #The input should be converted to an integer for it to be able to compare with the chosen number. This is a run-time error because it crashes the program when it tries to compare a string to an integer.
        guess= int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        #if guess == number_to_guess:
         #   print("Congratulations! You've guessed the number!")
          #  game_over = True
          #This if statement should be moved to the end and made as an elif statement attached to the if statement above this one. This is so it won't print Too high or too low when the player runs out of attempts (all one conditional). This is a logic error.
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1 #This must be added so that attempts>= max_attempts can be reached so the user will not have infinite attempts. This is a logic error.
        elif guess < number_to_guess:
            print("Too low! Try again.") 
            attempts += 1 #This must be added so that attempts>= max_attempts can be reached so the user will not have infinite attempts. This is a logic error.
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True 
        #continue
        #This continue statement is not needed as it does not change anything and is therefore redundant. This is a logic error.
    print("Game Over. Thanks for playing!")
start_game()