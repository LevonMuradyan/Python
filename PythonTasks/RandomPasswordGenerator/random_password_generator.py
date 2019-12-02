#!/usr/bin/env python

import string
import random
import sys

#Password generator menu, there are some commands to control:
#You can see the rules, start the checking and quit:
def password_menu():
    
    #Untill you quit:
    while True:

        print "********************************************"
        print "********************************************"
        print " Press (r) to see the password creating rules "
        print " Press (s) to start generating password "
        print " Press (q) or (Ctrl+C) to quit "
        print "********************************************"
        print "********************************************\n"
        
        try:
            controller = raw_input("Please enter one of these commands - ")
            
            #Checking for rules and open password_riles.txt:    
            if controller == 'r':
                rules = open("password_rules.txt","r")
                print rules.read()
                rules.close()
            #Checking for quit: 
            elif controller == 'q':
                raise KeyboardInterrupt
            #Checking for start:
            elif controller == 's':
                print "\nIf you want to create strong password be aware that length must be at least 12-digits"
                password_length = int(raw_input("Please enter the password length: "))
                print "\nPassword type must be weak, normal, good,strong\n"
                print "If you want to create password with 1 type of letters, write weak"
                print "If you want to create password with 2 type of letters, write normal"
                print "If you want to create password with 3 type of letters, write good"
                print "If you want to create password with all type of letters, write strong\n"

                password_type = raw_input("Please enter type of password: ")
                random_password_generator(password_length, password_type)      
            #Checking for other commands
            else:
                print "\nInvalid command, try again!!!\n"
        
        except ValueError:
            print "\nYou wrote characters" 
            print "Please write number !!!\n"

        #`Ctrl+C` handling
        except KeyboardInterrupt:
            print "\n\nYou pressed `Ctrl+C` or `q` and exit the program"
            print "If you want to generate password, please execute again!!!\n"
            sys.exit()


#This program generate passord by password length, password type
def random_password_generator(password_length, password_type):

    '''Function is generate password by length and type
    Args:
        password_length(int): The length of generating password
        password_type(str): The Password can be weak, normal, good, strong
    
    Raises:
        ValueError: if it can't be converted to int
        KeyboardInterrupt: if we push `Ctrl+c`

    Returns:
        str: generated password
    '''
   
    #Saving each type of letter into list   
                    
    symbols = [random.choice(string.punctuation) for character in range(password_length)]
    lowercase = [random.choice(string.ascii_lowercase) for lower in range(password_length)]
    uppercase = [random.choice(string.ascii_uppercase) for upper in range(password_length)]
    numbers = [random.choice(string.digits) for number in range(password_length)]
        
    letters_dict = {1:symbols,2:lowercase,3:uppercase,4:numbers}
    password = ''   
    #if password type is weak than use only one of the elements of letters_dict
    if password_type == "weak":

        rand = random.randint(1,4)
        generated_password = ''.join(letters_dict[rand])
        password = ''.join(random.choice(generated_password) for value in range(password_length))

    #if password type is normal than use only two of the elements of letters_dict
    elif password_type == "normal":
        rand = list(random.sample(range(1,4),2))
        generated_password = ''.join(letters_dict[rand[0]]+letters_dict[rand[1]])
        password = ''.join(random.choice(generated_password) for value in range(password_length))
  
    #if password type is good than use only three of the elements of letters_dict
    elif password_type == "good":
        rand = list(random.sample(range(1,4),3))
        generated_password = ''.join(letters_dict[rand[0]]+letters_dict[rand[1]]+letters_dict[rand[2]])
        password = ''.join(random.choice(generated_password) for value in range(password_length))
    
    #if password type is strong than use all the elements of letters_dict
    elif password_type == "strong" and password_length > 11:             
        generated_password = ''.join(symbols + lowercase + uppercase + numbers)
        password = ''.join(random.choice(generated_password) for value in range(password_length))
    
    #if password type is unrecognized than print Invalid input
    else:
        print "\nInvalid input\n"
        return
            
    print "\nYour password is = ",password,"\n"
    

if __name__ == "__main__":
    print random_password_generator.__doc__
    password_menu()
