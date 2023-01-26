from datetime import date
import pandas as pd  # Easier way to import and work with .csv files
import os

# get path to the files
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
        return f'Total: {x}'

    # subclass inventory yesterday
    def inventory_yesterday(self):
        dic_yesterday = {'item': [self.item],
                         'count': [self.sold_yesterday],
                         'Buy price': [self.price],
                         'Expiration Day': [self.expiration_date]}
        df = pd.DataFrame(data=dic_yesterday)
        pd.set_option('display.colheader_justify', 'center')
        x = df.to_string(index=False)
        return (x)

    # subclass inventory today

    def inventory_today(self):
        dic_today = {'item': [self.item],
                     'count': [self.sold_today],
                     'Buy price': [self.price],
                     'Expiration Day': [self.expiration_date]}
        df = pd.DataFrame(dic_today)
        pd.set_option('display.colheader_justify', 'center')
        x = df.to_string(index=False)
        return (x)

    # Subclass inventory. What it remains in the storage
    def in_storage(self):
        x = sum([self.sold_before_yesterday,
                 self.sold_yesterday, self.sold_today])
        y = self.amount - x
        return f" there is {y} kgs of {self.item} in storage"

    # Subclass Calculte revenue
    def revenue(self, date):
        if date == 'before_yesteday':
            cost = self.sold_before_yesterday * self.price
            collected = self.sold_before_yesterday * self.sell_price
            outcome = collected - cost
            return f"Reveue from before yesterday is {outcome} euros"
        elif date == 'yesterday':
            cost = self.sold_yesterday * self.price
            collected = self.sold_yesterday * self.sell_price
            outcome = collected - cost
            return f"Reveue from yesterday is {outcome} euros"
        elif date == 'today':
            cost = self.sold_today * self.price
            collected = self.sold_today * self.sell_price
            outcome = collected - cost
            return f"Reveue from before today is {outcome} euros"
        else:
            return 'Error. oops something went wrong'

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

    def order_produt(self, quantity):
        total_sold = sum([self.sold_before_yesterday,
                          self.sold_yesterday, self.sold_today])
        total_instorage = self.amount - total_sold

        if quantity <= total_instorage:
            outcome = total_instorage - quantity
            price = outcome * self.sell_price
            return f"you can buy {quantity} kgs of {self.item}for $ {price}.\nThere is {outcome} Kgs left in Storage"
        return f"Sorry we cannot sell you {self.item}.\nYou request is larger than our storage, We only have {total_instorage} kgs in storage"


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
        return f"{item} is not in inventory, you should try:\n{items_list}"


# print(items_details("orange").order_produt(40))
