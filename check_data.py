import pandas as pd

df = pd.read_csv("dataset/sales_data.csv", encoding="latin1")

print(df.head())
print(df.columns.tolist())
print(df.shape)