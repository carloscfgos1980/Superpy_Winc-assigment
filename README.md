## SUPERPY BUILDING PROCESS

# call the app in the terminal:
python3 superpy.py

I include a folder with everything I need to rearch to make this app works:
1. Parse (stdin, stdout, command line argsparse)
2. other (date)
3. csv (alll related of how to use pandas in csv)

# Steps:
1. Create product.py
1.1 Import modules
1.2 Get path to the files
1.3 Storing the data of the .csv files in variables
1.4 create a class (Product) to storage all the data from the csv
1.5 Create subclases in order to calculate inventory and check if ithe product is still fresh
1.6 Create a function that itirates trhu the list of items in order to assign values to class Product

2. Create all_products.py
2.1 Import modules
2.2 Get path to the files
2.3 Storing the data of the .csv files in variables
2.4 Create a List with the item's name
2.5 Create a list with the initial amount
2.6 Get the values of the columns of sold products and calculate the total sold
2.7 Built a dictionary to calculate de amount of items in storage
2.8 Calculate the amount of items in Storage
2.9 Get a DataFrame that shos all the items in storage

3. Change main.py into superpy.py
3.1 Import modules
3.2 Get path to the files
3.3 Storing the data of the .csv files in variables
3.4 Create: argParser = argparse.ArgumentParser
3.5 add.arguments
3.6 inside def main:
3.6.1 - message with command line explanation to get general data
3.6.2 - Need to implement a condiction to avoid the argsparse error
3.6.3 - implement try-except for catching error when an item is introduct and it doesn't exist in the inventory (list_items). 
I need to use this everytime except when I call the function without subclasss. Ex:
print(product.items_details(args.item))
Ex of call the function with subclasses:
print(product.items_details(args.fresh_product).fresh_item())
3.6.6 - End the if else with another condiction to create an input command that will provide me the general data. Here is were I print the message create in step (3.6.1)

## THE END

