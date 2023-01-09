# testing project for rock-paper-scissor game

import random

def game():
    user = input("'r' for rock, 'p' for paper, 's' for scissor")
    computer = random.choice(['r','p','s'])

    # setting rules of the game
    # given the rules of the game stated r > s , p > r , s > p
    if user == computer:
        return "tie"
    if winner(user,computer):
        return "you won!"
    else:
        return "you lost, try again"

#setting the logic of the game
def winner(player , opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r')\
        or (player == 's' and opponent == 'p'):
        return True

print(game())
