# Imports
import argparse
'''import csv'''  # I will use Pandas instead
import pandas as pd  # Easier way to import and work with .csv files
import os
import product

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    # print('BOUGHT \n:', data_bought)
    # print('SOLD \n:', data_sold)
    print(product.items_details('orange'))
    print(product.items_details('graves'))


path = os.getcwd()
path_to_file_bought = os.path.join(path, "bought.csv")
path_to_file_sold = os.path.join(path, "sold.csv")

argParser = argparse.ArgumentParser(
    prog='My Program',
    description='Manage the inventory of the store',
    epilog='Text at the bottom of help')

# Parse arguments
argParser.add_argument(
    "-i", "--item", help="input an item")
argParser.add_argument(
    "-y", "--yesterday", help="inventory yesterday")
argParser.add_argument(
    "-t", "--today", help="inventory today")
argParser.add_argument(
    "-s", "--storage", help="Storage")
argParser.add_argument(
    "-r2", "--revenue_before_yesterday", help="Revenues before yesterday")
argParser.add_argument(
    "-r1", "--revenue_yesterday", help="Revenues yesterday")
argParser.add_argument(
    "-r", "--revenue_before_today", help="Revenues before today")
argParser.add_argument(
    "-f", "--fresh_product", help="Type an item to check if it is not outdated")

args = argParser.parse_args()


# Storing the data of the .csv files in variables
data_bought = pd.read_csv(path_to_file_bought)
data_sold = pd.read_csv(path_to_file_sold)

# create a class to storage all the data from the csv


if __name__ == "__main__":
    main()
