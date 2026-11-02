# Rock Paper Scissors game

#
# USER SELECTION
#

VALID_CHOICES = ["rock", "paper", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors':\n> ").lower()
print("USER CHOICE:", u)
if u not in VALID_CHOICES:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

from random import choice

c = choice(VALID_CHOICES)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("USER WINS")
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("COMPUTER WINS") 
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")