import pandas as pd

df = pd.read_csv("data/persons.csv")

print(df.head())

df = df.drop_duplicates()

df = df.dropna()

print("Cleaned Data:")
print(df)