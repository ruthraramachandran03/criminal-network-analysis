import pandas as pd

# Read persons data
df = pd.read_csv("data/persons.csv")

print("Entity Linking Started")

for index, row in df.iterrows():
    print(row["person_id"], "->", row["name"])

print("\nEntity Linking Completed")