import sys
import random

print('')
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)
if player < 1 | player > 3:
    sys.exit("you must enter 1, 2 or 3.")
    

computerchoice = random.choice("123")

compuetr = int(computerchoice)

print("")
print("you chose " + playerchoice + ".")
print("python chose " + computerchoice + ".")

print("")