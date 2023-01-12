import sys


def motherfucker():
    return "what'z motherfucker"


inp = input("Type <-m> for motherfucker:\n")

# prints inp

if inp == '-m':
    print(sys.stdout.write(motherfucker()))


'''
def checking():
    for line in sys.stdin:
        if '-m' == line.rstrip():
            return sys.stdout.write(motherfucker())
        
    return False


print(checking())
'''
