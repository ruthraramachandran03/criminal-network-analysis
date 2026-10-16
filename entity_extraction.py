import pandas as pd

# Read persons data
df = pd.read_csv("data/persons.csv")

print("Extracted Person Entities:")

print(df[["person_id", "name"]])

print("\nTotal Persons:", len(df))