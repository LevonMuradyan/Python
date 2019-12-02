#!/usr/bin/env python

#Importing necessary modules:
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
                rules = open("cow_bull_rules.txt","r")
                print rules.read()
                rules.close()
            #Checking for quit: 
            elif controller == 'q':
                raise KeyboardInterrupt
            #Checking for start:
            elif controller == 's':
                print "\nWelcome to Cows and Bulls game :D\n"
                digits_count = input("Enter number of digits = ")
                cow_bull_game(digits_count)
            #Checking for other commands
            else:
                print "\nInvalid command, try again!!!\n"
        #`Ctrl+C` handling
        except KeyboardInterrupt:
            print "\nYou pressed `Ctrl+C` or `q` and exit the program"
            print "If you want to play, please execute again!!!\n"
            sys.exit()


def cow_bull_game(digits_count):
    
    '''Game that need to find a number

    Args:
        digits_count (int): The amount of number digits 

    Raises:
        ValueError: if string can't be converted to an integer
        KeyboardInterrupt: if we push 'Ctrl+c'
        
    Returns:
        void
    '''
 
    #Generate list of random integer of length digits_count
    
    first = 10**(digits_count-1)
    last = 10**digits_count-1

    num = [int(i) for i in str(random.randint(first, last))]
    print "\nSecret number =",num

    guess_count=0
    while True:
        guess_count+=1
        print "\nGuess:",guess_count


        while True:

            try:
                #User input like a string,if it can't be converted to an integer than call exception ValueError:
                guess = int(raw_input("Please guess " + str(digits_count) + "-digit number: "))
                
                #Transform input integer (e.g. 1234) to list of integers (e.g. [1,2,3,4]):
                guess = [int(i) for i in str(guess)]
                
                #Check if the given number digits count less than 4 call exception ValueError:
                if len(guess) != digits_count:
                    raise ValueError

                #Breaking loop ,if all are right:
                break
              
            except ValueError:
                print "\nYou wrote characters or number doesn't containing exactly" ,digits_count, "digits" 
                print "Please write" ,digits_count, "-digit number between" ,first, "and" ,last, "!!!\n"
  
            except KeyboardInterrupt:
                print "\nYou pressed Ctrl+C and exit the program"
                print "If you want to play, please execute again!!!\n"
                sys.exit()

        if guess == num:
            print "\nYou won. Congratulations!!!"
            print "It took you",guess_count,"guess(es).\n"
            break

        else:
            cow=0
            bull=0

            for x in range(0,digits_count):
                if guess[x]==num[x]:
                    cow += 1
                # look if digit is somewhere else in the solution key (might already be a cow)
                elif guess[x] in num:
                    bull += 1

        print "Cows:",cow,"Bulls:",bull

if __name__ == "__main__": 
    game_menu()
