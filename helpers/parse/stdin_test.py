# Read Input From stdin in Python using sys.stdin

'''
First we need to import sys module. sys.stdin can be used to get input from the command line directly. It used is for standard input. It internally calls the input() method. Furthermore, it, also, automatically adds ‘\n’ after each sentence.
'''
# Example: Taking input using sys.stdin in a for-loop
import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'Input : {line}')

print("Exit")

# Read Input From stdin in Python using input()
'''
The input() can be used to take input from the user while executing the program and also in the middle of the execution.
'''

# this accepts the user's input
# and stores in inp
inp = input("Type anything")

# prints inp
print(inp)


def motherfucker():
    return "what'z motherfucker"


print(motherfucker)
