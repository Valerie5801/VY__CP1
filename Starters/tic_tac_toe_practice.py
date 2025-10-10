import random


def game():
    while True:
        comp_choice = random.randint(1, 9)
        player_choice = int(input("Please choose a spot (1-9): "))
        if player_choice in board:
            choice_index = board.index(player_choice)
            board[choice_index] = "O"
        elif player_choice not in board:
            print("That isn't a valid option.")
            continue
        comp_index = board.index(comp_choice)
        b
        #IM TIRED
