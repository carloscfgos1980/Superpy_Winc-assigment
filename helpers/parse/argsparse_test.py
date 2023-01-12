import argparse

argParser = argparse.ArgumentParser(
    prog='My Program',
    description='What the program does',
    epilog='Text at the bottom of help')

argParser.add_argument(
    "-n", "--name", help="con este comando vas a manejar el nombre")

argParser.add_argument(
    "-c", "--salud_now", help="bla, bla, bla")

args = argParser.parse_args()


def motherfucker(name):
    return f"What'z up, {name}!"


def salut_now():
    return "What'z up, motherfucker!"


print(motherfucker(args.name))
print(args.salud_now())
