"""
CP1401 2021-1 Assignment 1
Program 2 – Tennis Results
Student Name: Braydan Newman
Date started: 21/3/2021
Date completed: 21/3/2021
Pseudocode:

    set fast game point

    get player 1 score
    get player 2 score

    total games played = player 1 score + player 2 score

    if player 1 score > player 2 score
        display you won
    elif player 2 score > player 1 score
        display you lost
    else
        display draw

    if total games played >= 8
        display fast game

"""

# Declare all consents
FAST_GAME_POINT = 8

print("Welcome Player 1. How was your match?")

# Collect all user input
player1_score = int(input("    Your score: "))
player2_score = int(input("Opponent score: "))

# Calculate all necessary components
total_games = player1_score + player2_score

# Decides who won the game and prints appropriate output
if player1_score > player2_score:
    print("You Won :)")
elif player2_score > player1_score:
    print("You lost :( Keep trying.")
else:
    print("It's a draw.")

# Decides whether the game fast and prints appropriate output
if total_games >= FAST_GAME_POINT:
    print("Congratulations on playing a fast match!")
