import argparse
'''
import os

path = os.getcwd()

for f in os.listdir(path):
    print(f)
'''
argParser = argparse.ArgumentParser(
    prog='My Program',
    description='Manage the inventory of the store',
    epilog='Text at the bottom of help')

argParser.add_argument(
    "-n", "--name", help="con este comando vas a manejar el nombre")
argParser.add_argument(
    "-e", "--element", help="con este comando vas a a comprobar algo")

args = argParser.parse_args()


def checking(el):
    return f'Checking this {el}'


print(checking(args.element))
'''
print("args=%s" % args)

print("args.name=%s" % args.name)
'''
