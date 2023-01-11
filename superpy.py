# Imports
import argparse
'''import csv'''  # I will use Pandas instead
import pandas as pd  # Easier way to import and work with .csv files
import os
import sys
import product
import all_products_data

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    msg_items_bought = "Type <-B> in order to check all bought itmes data:\n"
    msg_items_sold = "Type <-S> in order to check all bought itmes data:\n"
    msg_storage_update = "Type <-U> in order to check all bought itmes data:\n"
    msg_item = "Type <-i> for all item data:\n"
    msg_inventory_yesterday = "Type<-y> to check the inventory from yesterday:\n"
    msg_inventory_today = "Type<-t> to check the inventory from today:\n"
    msg_item_storage = "Type<-s> to check the amount of item in the storage:\n"
    msg_revenue_before_yesterday = "Type<-r2> to check the revenue from before yesterday:\n"
    msg_revenue_yesterday = "Type<-r1> to check the revenue from yesterday:\n"
    msg_revenue_today = "Type<-r> to check the revenue from before today:\n"
    msg_fresh_item = "Type<-f> to check if the item is not outdated:\n"

    msg = msg_items_bought + msg_items_sold + msg_storage_update + msg_item + msg_inventory_yesterday + \
        msg_inventory_today + msg_item_storage + \
        msg_revenue_before_yesterday + msg_revenue_yesterday + \
        msg_revenue_yesterday + msg_revenue_today + msg_fresh_item
    # print(product.items_details('orange').inventory_yesterday())
    print(product.items_details(args.item))

    print(product.items_details(args.yesterday).inventory_yesterday())
    '''
    print(product.items_details(args.today).inventory_today())
    print(product.items_details(args.storage).in_storage())
    print(product.items_details(args.revenue_before_yesterday).revenue(
        'before_yesterday'))
    print(product.items_details(args.revenue_yesterday).revenue(
        'yesterday'))
    print(product.items_details(args.revenue_today).revenue(
        'today'))
    print(product.items_details(args.fresh_product).fresh_item())
    '''
    print(msg)
    inp = input("Type one command:\n")
    if inp == '-B':
        print(data_bought)
    elif inp == '-S':
        print(data_sold)
    elif inp == '-U':
        print(all_products_data.storage_data())

    # print('BOUGHT \n:', data_bought)
    # print('SOLD \n:', data_sold)
    print(product.items_details('orange'))
    print(product.items_details('graves'))
    print(product.items_details('orange').total_sold)
    # print(all_products_data.storage_data())


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
data_bought = pd.read_csv(path_to_file_bought, index_col=False)
pd.set_option('display.colheader_justify', 'center')

data_sold = pd.read_csv(path_to_file_sold, index_col=False)
pd.set_option('display.colheader_justify', 'center')

if __name__ == "__main__":
    main()
