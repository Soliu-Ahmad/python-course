import sys
import random
from enum import Enum

def play_rps():
    
    class Choice(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3 

    playerchoice = input("\nEnter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
    
    if playerchoice not in ['1', '2', '3']:
        print("you must enter 1, 2 or 3.")
        return play_rps()   
        
    player = int(playerchoice)
    
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
    
    print("\nPlay again? ")
    
    while True:
            
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ['y', 'q']:
            # print("you must enter Y or Q.")
            continue
        else:
            break
    
    if playagain.lower() == 'y':
            return play_rps()        
        
    else:
            print("Thanks for playing!\n")
            playagain = False 
            sys.exit("Bye!")
play_rps()