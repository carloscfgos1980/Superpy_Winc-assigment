# Imports
import argparse
'''import csv'''  # I will use Pandas instead
import pandas as pd  # Easier way to import and work with .csv files
import os
import product
import all_products_data

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    msg_items_bought = "Type <-B> in order to check all bought itmes data:\n"
    msg_items_sold = "Type <-S> in order to check all sold itmes data:\n"
    msg_storage_update = "Type <-U> in order to check all itmes data in storage:\n"
    # message with command line explanation to get general data
    msg = msg_items_bought + msg_items_sold + msg_storage_update

    # Need to implement a condiction to avoid the argsparse error
    if args.yesterday:
        try:
            print(product.items_details(args.yesterday).inventory_yesterday())
        except AttributeError:  # This avoid the error when a non-existance item is typed
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.today:
        try:
            print(product.items_details(args.today).inventory_today())
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.storage:
        try:
            print(product.items_details(args.storage).in_storage())
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.revenue_before_yesterday:
        try:
            print(product.items_details(args.revenue_before_yesterday).revenue(
                'before_yesterday'))
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.revenue_yesterday:
        try:
            print(product.items_details(args.revenue_yesterday).revenue(
                'yesterday'))
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.revenue_today:
        try:
            print(product.items_details(args.revenue_today).revenue(
                'today'))
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.fresh_product:
        try:
            print(product.items_details(args.fresh_product).fresh_item())
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.item and args.quantity:
        try:
            print(product.items_details(args.item).order_produt(args.quantity))
        except AttributeError:
            print(
                f"We don't have this product. You should try: \n{all_products_data.items_list}")
            return True
    elif args.item:
        print(product.items_details(args.item))
    else:
        print(msg)
        inp = input("Type one command:\n")
        if inp == '-B':
            print(data_bought)
        elif inp == '-S':
            print(data_sold)
        elif inp == '-U':
            print(all_products_data.storage_data())


# getting path
path = os.getcwd()
path_to_file_bought = os.path.join(path, "bought.csv")
path_to_file_sold = os.path.join(path, "sold.csv")

# Storing the data of the .csv files in variables
data_bought = pd.read_csv(path_to_file_bought, index_col=None)
pd.set_option('display.colheader_justify', 'center')

data_sold = pd.read_csv(path_to_file_sold, index_col=None)
pd.set_option('display.colheader_justify', 'center')

# Args parse allows me to pass the parameter from the command line
argParser = argparse.ArgumentParser(
    prog='My Program',
    description='Manage the inventory of the store',
    epilog='Text at the bottom of help')

# Parse arguments
argParser.add_argument(
    "-i", "--item", type=str, help="input an item")
argParser.add_argument(
    "-q", "--quantity", type=float, help="input an quanty of the desireable item")
argParser.add_argument(
    "-y", "--yesterday", type=str, help="inventory yesterday")
argParser.add_argument(
    "-t", "--today", type=str, help="inventory today")
argParser.add_argument(
    "-s", "--storage", type=str, help="Storage")
argParser.add_argument(
    "-r2", "--revenue_before_yesterday", type=str, help="Revenues before yesterday")
argParser.add_argument(
    "-r1", "--revenue_yesterday", type=str, help="Revenues yesterday")
argParser.add_argument(
    "-r", "--revenue_today", type=str, help="Revenues before today")
argParser.add_argument(
    "-f", "--fresh_product", type=str, help="Type an item to check if it is not outdated")

# This I will use for the argsparse
args = argParser.parse_args()  # Example args.item


if __name__ == "__main__":
    main()
