# user plays a round of Rock, Paper, Scissors against the computer.
# Rock beats Scissors, Scissors beat Paper, Paper beats Rock
# Create player and computer variables to compare
player = 0
computer = 0

# Store player 1's input: 1 is for '✊' (Rock); 2 is for '✋' (Paper); 3 is for '✌️' (Scissors).
player = int(input("Pick a number between 1 and 3"))
if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
else:
    print("Invalid response! Youy automatically loose")

# Use random.randint() method to assign a number to the computer variable (1 to 3).
import random
computer = random.randint (1,3)
if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
elif computer == 3 :
    print("CPU chose: ✌️")
else:
    print("Invalid response! Youy automatically loose")

# Recognize the winner
if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 2:
    print("Computer wins!")
elif player == 1 and computer == 3:
    print("Player wins!")
elif player == 2 and computer == 1:
    print("Player wins!")
elif player == 2 and computer == 3:
    print("Computer wins!")
elif player == 3 and computer == 1:
    print("Computer wins!")
else:
    print("Player wins!")