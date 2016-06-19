# Rock-paper-scissors-lizard-Spock

import random

def name_to_number(name):
    name = name.lower() # when input is uppercase, this make it lowercase
    if (name == "rock"):
        return 0
    elif (name == "spock"):
        return 1
    elif (name == "paper"):
        return 2
    elif (name == "lizard"):
        return 3
    elif (name == "scissors"):
        return 4
    else:
        print "Error: Player chose an unknown string."
        return 10
                    
def number_to_name(number):
    if (number == 0):
        return "rock"
    elif (number == 1):
        return "Spock"
    elif (number == 2):
        return "paper"
    elif (number == 3):
        return "lizard"
    elif (number == 4):
        return "scissors"
    else:
        print "Error: Entered a wrong number."
    
def rpsls(player_choice): 
    print ""
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    if(player_number == 10): # when input is wrongly spelt or different
        print "No one wins! as player chose wrong string."
    else: # when input is correctly spelt or correct
        difference = (comp_number - player_number) % 5
        if(difference == 0):
            print "Player and computer Tie!"
        elif ( 1 <= difference <=2):
            print "Computer wins!"
        elif ( 3<= difference <= 4):
            print "Player wins!"
        else:
            print "Error"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")