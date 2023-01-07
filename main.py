# Imports
import argparse
import csv
from datetime import date
import pandas as pd
import os

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    print('BOUGHT \n:', data_bought)
    print('SOLD \n:', data_sold)
    print(data_bought.values[1][2])
    print(data_sold.values[1][2])
    print('ORANGE:\n', orange)
    print('POTATO:\n', potato)
    print('BANANA:\n', banana)
    print('APPLE:\n', apple)
    print('MEAT:\n', meat)
    print(orange.total_sold())
    print(orange.in_storage())
    print('REVENUE FROM YESTREDAY BANANA SELLING:\n',
          banana.revenue('yesterday'))


'''
def bought_items():
    outcome = []
    with open('bought.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            outcome.append(row)
    return outcome
'''
path = os.getcwd()
path_to_file_bought = os.path.join(path, "bought.csv")
path_to_file_sold = os.path.join(path, "sold.csv")

data_bought = pd.read_csv(path_to_file_bought)
data_sold = pd.read_csv(path_to_file_sold)


class Product():
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

    def __str__(self):
        return f"Item: {self.item}\nprice: {self.price}\namount: {self.amount} kgs\nsell price: {self.sell_price}\nsold before yesterday: {self.sold_before_yesterday}\nsold yesterday: {self.sold_yesterday}\nsold today: {self.sold_today}\nbuy date: {self.buy_date}\nexpiration date: {self.expiration_date}"

    def total_sold(self):
        x = sum([self.sold_before_yesterday,
                self.sold_yesterday, self.sold_today])
        return x

    def in_storage(self):
        y = self.amount - self.total_sold()
        return y

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


orange = Product(data_bought.values[0][1], data_bought.values[0][2], data_bought.values[0][3], data_sold.values[0][5],
                 data_sold.values[0][2], data_sold.values[0][3], data_sold.values[0][4], data_bought.values[0][4], data_bought.values[0][5])

potato = Product(data_bought.values[1][1], data_bought.values[1][2], data_bought.values[1][3], data_sold.values[1][5],
                 data_sold.values[1][2], data_sold.values[1][3], data_sold.values[1][4], data_bought.values[1][4], data_bought.values[1][5])

banana = Product(data_bought.values[2][1], data_bought.values[2][2], data_bought.values[2][3], data_sold.values[2][5],
                 data_sold.values[2][2], data_sold.values[2][3], data_sold.values[2][4], data_bought.values[2][4], data_bought.values[2][5])

apple = Product(data_bought.values[3][1], data_bought.values[3][2], data_bought.values[3][3], data_sold.values[3][5],
                data_sold.values[3][2], data_sold.values[3][3], data_sold.values[3][4], data_bought.values[3][4], data_bought.values[3][5])

meat = Product(data_bought.values[4][1], data_bought.values[4][2], data_bought.values[4][3], data_sold.values[4][5],
               data_sold.values[4][2], data_sold.values[4][3], data_sold.values[4][4], data_bought.values[4][4], data_bought.values[4][5])

if __name__ == "__main__":
    main()
