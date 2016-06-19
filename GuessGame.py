# "Guess the number"

import random
import simplegui
import math

def new_game():
    print
    print "New game. Range is from 0 to 100"
    print "Number of guesses remaining is 7"
    global secret_number, counter, counter_range
    counter_range = False
    counter = 7
    secret_number = random.randrange(0,100)
    
def range100():
    new_game()
    
def range1000():
    print 
    print "New game. Range is from 0 to 1000"
    print "Number of guesses remaining is 10"
    global secret_number, counter, counter_range
    counter_range = True
    secret_number = random.randrange(0,1000)
    counter = 10
    
def input_guess(guess):
    print
    global counter, secret_number, counter_range
    counter = counter - 1
    guess = int(guess)
    print "Guess was", guess
    print "Number of remaining guesses", counter
    if counter == 0 or guess == secret_number:
        if guess != secret_number:
            print "You ran out of guesses. The number was", secret_number
        else:
            print "Correct!"
        if counter_range:
            range1000()
        else:
            new_game()
    elif (guess < secret_number):
        print "Higher!"
    else:
        print "Lower!"
        
# create frame
frame = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()