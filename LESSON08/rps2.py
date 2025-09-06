import sys
import random
from enum import Enum

class Choice(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True
while playagain:
 
    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("you must enter 1, 2 or 3.")
        
    computerchoice = random.choice("123")   

    compuetr = int(computerchoice)

    
    print("\nYou chose " + str(Choice(player)).replace("Choice.", "") + ".")
    print("python chose " + str(Choice(compuetr)).replace("Choice.", "") + ".\n")


    if player == 1 and compuetr == 3:
        print("you win!")
    elif player == 2 and compuetr == 1:
        print("you win!")
    elif player == 3 and compuetr == 2:
        print("you win!")
    elif player == compuetr:
        print("it's a tie!")
    else:    
        print("you lose!")

    # print("")
    # again = input("Play again? (y/n): ")
    # if again.lower() != 'y':
    #     playagain = False
    #     print("Thanks for playing!")
    playagain = input("\nPlay again?  \nY for Yes or \nQ to Quit:\n\n")
    
    if playagain.lower() == 'y':
        continue
    else:
        print("Thanks for playing!\n")
        playagain = False
        sys.exit("Bye!")