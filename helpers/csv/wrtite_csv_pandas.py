import pandas as pd  # Easier way to import and work with .csv files


df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})

x = df.to_csv(index=False, sep='|', encoding='utf-8', lineterminator='\n')
print(x)
