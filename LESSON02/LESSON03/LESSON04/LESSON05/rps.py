import sys
import random
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
# print(Choice(2))
# print(Choice.ROCK)
# print(Choice["ROCK"])
# print(Choice.ROCK.value)
# sys.exit()

print('')
playerchoice = input("Enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)
if player < 1 or player > 3:
    sys.exit("you must enter 1, 2 or 3.")
    

computerchoice = random.choice("123")   

compuetr = int(computerchoice)

print("")
print("you chose " + str(Choice(player)).replace("Choice.", "") + ".")
print("python chose " + str(Choice(compuetr)).replace("Choice.", "") + ".")

print("")

if player == 1 and compuetr == 3:
    print("you win!")
elif player == 2 and compuetr == 1:
    print("you win!")
elif player == 3 and compuetr == 2:
    print("you win!")
elif player == compuetr:
    print("it's a tie!")
else:    
    print("you win!")