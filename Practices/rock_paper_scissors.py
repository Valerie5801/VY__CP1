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
        player_score = 0
        comp_score = 0
        while True:
            player_choice = input("Choose rock, paper, or scissors: ")
            if player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
                print("That is not a valid option. Try again.")
                continue
            else:
                comp_choice = options[random.randint(0, 2)]
                print(f"You chose: {player_choice}")
                print(f"Computer chose: {comp_choice}")
                if comp_choice == "rock":
                    if player_choice.strip().lower() == "rock":
                        print("It's a tie.")
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "paper":
                        print("You win!")
                        player_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "scissors":
                        print("You lost.")
                        comp_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                        
                elif comp_choice == "paper":
                    if player_choice.strip().lower() == "rock":
                        print("You lost.")
                        comp_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "paper":
                        print("It's a tie.")
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "scissors":
                        print("You win!")
                        player_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")

                elif comp_choice == "scissors":
                    if player_choice.strip().lower() == "rock":
                        print("You win!")
                        player_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "paper":
                        print("You lost.")
                        comp_score += 1
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")
                    elif player_choice.strip().lower() == "scissors":
                        print("It's a tie.")
                        print(f" Player score: {player_score}\n Computer score: {comp_score}")

                play_again = input("Play again?(y/n): ")
                if play_again == "y":
                    continue
                elif play_again == "n":
                    print(f"Thank you for playing. \nFinal scores are: \n\tPlayer score: {player_score} \n\tComputer score: {comp_score}")
                    break
    else:
        print("That isn't a valid option.")