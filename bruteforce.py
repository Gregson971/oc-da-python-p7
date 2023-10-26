import pandas as pd
from tabulate import tabulate

# Read the data
data = pd.read_csv('data/dataset_test_shares.csv')

print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
