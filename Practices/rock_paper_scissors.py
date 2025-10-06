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
            if player_choice.strip().lower() == "rock":
                print("It's a tie.")
            elif player_choice.strip().lower() == "paper":
                print("You win!")
            elif player_choice.strip().lower() == "scissors":
                print("You lost.")
                
        elif comp_choice == "paper":
            if player_choice.strip().lower() == "rock":
                print("You lost.")
            elif player_choice.strip().lower() == "paper":
                print("It's a tie.")
            elif player_choice.strip().lower() == "scissors":
                print("You win!")

        elif comp_choice == "scissors":
            if player_choice.strip().lower() == "rock":
                print("You win!")
            elif player_choice.strip().lower() == "paper":
                print("You lost.")
            elif player_choice.strip().lower() == "scissors":
                print("It's a tie.")
    else:
        print("That isn't a valid option")