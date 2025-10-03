#VY 2nd Rock Paper Scissors
import random
options = ["rock", "paper", "scissors"]

while True:
    play = input("Would you like to play?(y/n): ")
    if play == "n":
        print("Goodbye!")
        break
    elif play == "y":
        print("Let's begin.")
        player_choice = input("Choose rock, paper, or scissors: ")
        comp_choice = options[random.randint(0, 2)]
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {comp_choice}")
        if comp_choice == "rock":
            if player_choice == "rock":
                print("It's a tie.")
            if player_choice == "p":
                print()
    else:
        print("what do you want")