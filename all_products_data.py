import pandas as pd  # Easier way to import and work with .csv files
import os

# get path to the files
path = os.getcwd()
path_to_file_bought = os.path.join(path, "bought.csv")
path_to_file_sold = os.path.join(path, "sold.csv")

# Storing the data of the .csv files in variables
data_bought = pd.read_csv(path_to_file_bought)
data_sold = pd.read_csv(path_to_file_sold)
# print(data_bought)

# From data_bought (csv), create a list with the elements in the row (items)
items_list = []  # This is used in Error return in superpy.py so I need to imported there
for index, row in data_bought.iterrows():
    x = row["items"]
    items_list.append(x)

# From data_bought (csv), create a list with the elements in the row (initial amount of items)
initial_amount_list = []
for index, row in data_bought.iterrows():
    x = row["amount_kg"]
    initial_amount_list.append(x)

# Get the values of the columns of sold products and calculate the total sold
before_yesterday_list = []
yesterday_list = []
today_list = []
total_sold = []
for i in range(len(items_list)):
    before_yesterday = data_sold.values[i][3]
    before_yesterday_list.append(before_yesterday)
    yesterday = data_sold.values[i][4]
    yesterday_list.append(yesterday)
    today = data_sold.values[i][5]
    total = sum([before_yesterday, yesterday, today])  # getting total sold
    total_sold.append(total)

# Built a dictionary to calculate de amount of items in storage
cal_storage = {
    'sold': total_sold,
    'initial_amount': initial_amount_list
}
# Calculate the amount of items in Storage
in_storage_list = []
for i in range(len(items_list)):
    initial = cal_storage["initial_amount"][i]
    total_expended = cal_storage["sold"][i]
    in_storogae = initial - total_expended
    in_storage_list.append(in_storogae)

# get a DataFrame that shos all the items in storage


def storage_data():
    dic_storage = {
        'item': items_list,
        'initial amount': initial_amount_list,
        'sold': total_sold,
        'in storage': in_storage_list
    }
    # Convert the dictionary into DataFrame
    df = pd.DataFrame(
        data=dic_storage, columns=[
            'item', 'initial amount', 'sold', 'in storage'])
    pd.set_option('display.colheader_justify', 'center')  # format align center

    x = df.to_string(index=False)  # decapricate the index in the output doc
    return x
