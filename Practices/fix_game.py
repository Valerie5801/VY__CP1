#VY 2nd Fix the Game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #There's another issue with guess = int(input("Enter your guess: ")) being on this line: even if the user used all of their attempts, they can guess one more time but the program will only say that the user used all attempts. This is a logic error.
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        else:
            guess = input("Enter your guess: ") #The user input should be a number, but instead this input defaults to a string. When the computer tries to compare a string to a number, it breaks. This is a run-time error.
            if not guess.isdigit(): #This is a fail safe.
                print("Invalid input. Please put an integer.")
            else:
                if guess == number_to_guess: #This "if" statement (and all elifs below it) is suppoesd to be inside the above else statement because it should only run if the user still has attempts left. This is a logic error. This is a problem since even if the user loses the game, the program will still print "Too low" or "too high" before printing "Game over". This can quickly become annoying.
                    print("Congratulations! You've guessed the number!")
                    game_over = True
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                    attempts += 1 #(This also applies to the conditional below this one.) attempts += 1 must run after every time the user guesses incorrectly so there is a way for the user to lose. If attempts never reaches the max_attempts, there is no way that if attempts >= max_attempts will be true, so the user basically has unlimited attempts. This is a logic error.
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                    attempts += 1
        continue
    print("Game Over. Thanks for playing!")
start_game()