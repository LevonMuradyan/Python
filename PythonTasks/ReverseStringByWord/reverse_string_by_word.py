#!/usr/bin/env python
import sys


def reverse_string_by_word(string):
    '''Function that reverse string by words

    Args:
        string(str): The sentence need to be reversed by words
    
    Raises:
        KeyboardInterrupt: if we push `Ctrl+c`

    Returns:
        str: Reversed by words string
    '''
          
    return ' '.join(string.split(' ')[::-1])

"""
If you are running your module (the source file) 
as the main program, the interpreter will assign 
the hard-coded string "__main__" to the __name__ variable:
That's why `if` statement is true:

"""
if __name__ == "__main__":
    
    print reverse_string_by_word.__doc__   
    '''Exception for `Ctrl+C` handling:''' 
    try: 
        string = raw_input("Input string : ")
    except KeyboardInterrupt:
        print "\nYou pressed Ctrl+C, please write sentence!!!"
        sys.exit()
    
    print "Reversed string :",reverse_string_by_word(string)

