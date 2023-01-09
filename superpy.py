# Imports
import argparse
'''import csv'''  # I will use Pandas instead
from datetime import date
import pandas as pd  # Easier way to import and work with .csv files
import os

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    print('BOUGHT \n:', data_bought)
    print('SOLD \n:', data_sold)
    print(items_details('graves'))
    print(items_details('orange').fresh_item())


path = os.getcwd()
path_to_file_bought = os.path.join(path, "bought.csv")
path_to_file_sold = os.path.join(path, "sold.csv")

# Storing the data of the .csv files in variables
data_bought = pd.read_csv(path_to_file_bought)
data_sold = pd.read_csv(path_to_file_sold)

# create a class to storage all the data from the csv


class Product():
    today = date.today()  # method to obtain the current day

    def __init__(self, item, amount, price, sell_price, sold_before_yesterday, sold_yesterday, sold_today, buy_date, expiration_date):
        self.item = item
        self.amount = amount
        self.price = price
        self.sell_price = sell_price
        self.sold_before_yesterday = sold_before_yesterday
        self.sold_yesterday = sold_yesterday
        self.sold_today = sold_today
        self.buy_date = buy_date
        self.expiration_date = expiration_date

    # string that identify the item
    def __str__(self):
        return f"Item: {self.item}\nprice: {self.price}\namount: {self.amount} kgs\nsell price: {self.sell_price}\nsold before yesterday: {self.sold_before_yesterday}\nsold yesterday: {self.sold_yesterday}\nsold today: {self.sold_today}\nbuy date: {self.buy_date}\nexpiration date: {self.expiration_date}"

    # subclass to calcultate amount of itemts(kgs) that been sold
    def total_sold(self):
        x = sum([self.sold_before_yesterday,
                self.sold_yesterday, self.sold_today])
        return x

    # Subclass inventory. What it remains in the storage
    def in_storage(self):
        y = self.amount - self.total_sold()
        return y

    # Subclass Calculte revenue
    def revenue(self, date):
        if date == 'before_yesteday':
            cost = self.sold_before_yesterday * self.price
            collected = self.sold_before_yesterday * self.sell_price
            outcome = collected - cost
            return outcome
        elif date == 'yesterday':
            cost = self.sold_yesterday * self.price
            collected = self.sold_yesterday * self.sell_price
            outcome = collected - cost
            return outcome
        else:
            cost = self.sold_today * self.price
            collected = self.sold_today * self.sell_price
            outcome = collected - cost
            return outcome

    # Subclass Check if the product is still fresh
    def fresh_item(self):
        date1 = self.expiration_date
        y1, m1, d1 = [int(x) for x in date1.split('-')]
        expire_date = date(y1, m1, d1)
        if expire_date > self.today:
            delta = expire_date - self.today
            return f'{self.item} is still fresh and it will expire in {delta.days} days'
        else:
            return f'{self.item} has expired'


# From data_bought (csv), create a list with the elements in the row (items)
items_list = []
for index, row in data_bought.iterrows():
    x = row["items"]
    items_list.append(x)


# looping thru the list of items in order to dunamically pass arguments to the class Product
def items_details(item):
    if item in items_list:
        for i in range(len(items_list)):
            product = items_list[i]
            if product == item:
                product = Product(data_bought.values[i][1], data_bought.values[i][2], data_bought.values[i][3], data_sold.values[i][5],
                                  data_sold.values[i][2], data_sold.values[i][3], data_sold.values[i][4], data_bought.values[i][4], data_bought.values[i][5])
                return product
    else:
        return "this item is not in inventory"


if __name__ == "__main__":
    main()
