#!/usr/bin/env python

import random
import sys

#Game menu, there are some commands to control the game:
#You can see the rules, start the game and quit:
def game_menu():
    
    #Untill you quit the game:
    while True:

        print "********************************************"
        print "********************************************"
        print " Press (r) to see the game rules "
        print " Press (s) to start the game "
        print " Press (q) or (Ctrl+C) to quit the game "
        print "********************************************"
        print "********************************************\n"
        
        try:
            controller = raw_input("Please enter one of these commands - ")
            
            #Checking for rules and open cow_bull_rules.txt:    
            if controller == 'r':
                rules = open("guessing_game_rules.txt","r")
                print rules.read()
                rules.close()
            #Checking for quit: 
            elif controller == 'q':
                raise KeyboardInterrupt
            #Checking for start:
            elif controller == 's':
                guessing_game()
            #Checking for other commands
            else:
                print "\nInvalid command, try again!!!\n"
        #`Ctrl+C` handling
        except KeyboardInterrupt:
            print "\nYou pressed `Ctrl+C` or `q` and exit the program"
            print "If you want to play, please execute again!!!\n"
            sys.exit()

def guessing_game():

    '''Game that finding your number

    Args:
        None 

    Raises:
        KeyboardInterrupt: if we push 'Ctrl+c'
        
    Returns:
        void
    '''

    i = 0
    # i is the lowest number in range of possible guess
    j = 100
    # j is the highest number in range of possible guesses
    m = 50
    # m is the middle number in range of possible guesses
    counter = 0
    # counter is the number of guesses take.
    n=0
    
    print "\n(l) means it's too low" 
    print "(c) means it's your guess"
    print "(h) means it's too high\n "
    
    while True:
        n=m
        condition = raw_input("Is your guess " + str(m) + "?  ") 
        if condition == 'l':
            i = m + 1
            counter+=1
        elif condition == 'h':
            j = m - 1
            counter+=1
        elif condition == 'c':
            counter+=1
            break
        else:
            print "\nInvalid command, you must type one of these followings \n"
            print "\n(l) means it's too low" 
            print "(c) means it's your guess"
            print "(h) means it's too high\n "
        m = (i + j) / 2

        if n == j:
            print "You are kidding me it must be the number ",j 
            break 
        
        if n == i:
            print "You are kidding me it must be the number ",i
            break
        #m = (i + j) / 2
    print "\nIt took" , counter , "times to guess your number\n"

if __name__ == "__main__": 
    game_menu() 
