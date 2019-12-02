#!/usr/bin/env python

import sys

#Password Checking menu, there are some commands to control:
#You can see the rules, start the checking and quit:
def password_menu():
    
    #Untill you quit:
    while True:

        print "********************************************"
        print "********************************************"
        print " Press (r) to see the password creating rules "
        print " Press (s) to start checking password strongness "
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
                password = raw_input("\nEnter your password: ")
                check_password(password)      
            #Checking for other commands
            else:
                print "\nInvalid command, try again!!!\n"
        #`Ctrl+C` handling
        except KeyboardInterrupt:
            print "\nYou pressed `Ctrl+C` or `q` and exit the program"
            print "If you want to check password, please execute again!!!\n"
            sys.exit()

def check_password(password):    
    
    '''Function that check password strongness

    Args:
        password(str): The sentence need to be checked for strongness
    
    Raises:
        KeyboardInterrupt: if we push `Ctrl+c`

    Returns:
        str: Strongness type 
    '''

    #stores each boolean variables and strongness
    ll, ul, s, n, strongness =(0,0,0,0,0)
    
    #This loop calculate how many letters types there are       
    for char in password:

        if char.isdigit() and n==0:
            n=1
        elif char.islower() and ll==0:
            ll=1
        elif char.isupper() and ul==0:
            ul=1
        elif (char>='!' and char<='/') or (char>=':' and char<='@') \
            or (char>='[' and char<='`') or (char>='{' and char<='~') and s==0:       
            s=1
    
    strongness=ll+ul+n+s

    #According password rules there are some ways        
    if strongness == 0: 
        print "\nYou pressed Enter, write sentence!!!"
    elif strongness == 1:
        print "\nYour password is weak"
    elif strongness == 2:
        print "\nYour password is normal"
    elif strongness == 3:
        print "\nYour password is good"
    else:
        if len(password) < 12:
            print "\nYour password is good"
        else:    
            print "\nYour password is strong"
 

   
if __name__ == "__main__":
    print check_password.__doc__ 
    password_menu()
