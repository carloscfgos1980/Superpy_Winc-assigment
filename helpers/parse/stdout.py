# sys.stdout.write in Python
'''
This is a built-in Python module that contains parameters specific to the system i.e. it contains variables and methods that interact with the interpreter and are also governed by it. 

sys.stdout
A built-in file object that is analogous to the interpreter’s standard output stream in Python. stdout is used to display output directly to the screen console. Output can be of any form, it can be output from a print statement, an expression statement, and even a prompt direct for input. By default, streams are in text mode. In fact, wherever a print function is called within the code, it is first written to sys.stdout and then finally on to the screen. 

sys.stdout.write() serves the same purpose as the object stands for except it prints the number of letters within the text too when used in interactive mode. Unlike print, sys.stdout.write doesn’t switch to a new line after one text is displayed. To achieve this one can employ a new line escape character(\n).
'''

import sys


sys.stdout.write('gfg')
sys.stdout.write('geeks')
sys.stdout.write('\n')
sys.stdout.write('for geeks')

'''
stdout can be also be used to print multiple elements. Not just this stdout can be assigned to another variable as long as it supports write().
'''

# stdout assigned to a variable
var = sys.stdout
arr = ['geeks', 'for', 'geeks']

# printing everything in the same line
for i in arr:
    var.write(i)

# printing everything in a new line
for j in arr:
    var.write('\n'+j+'\n')


def motherfucker():
    return "what'z motherfucker"


sys.stdout.write(motherfucker())
