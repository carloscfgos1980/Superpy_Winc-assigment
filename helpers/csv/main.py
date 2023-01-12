import pandas as pd
import os
path = os.getcwd()
csv_file = "bought.csv"
path_to_file = os.path.join(path, csv_file)

df = pd.read_csv(path_to_file)
print(df)
print(df.values)
print(df.values[0])
print('check 1', df.columns[1])
print(df.values[1][1:3])
print(df.values[1][1])
