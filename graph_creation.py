import pandas as pd
from neo4j import GraphDatabase

# -----------------------------
# Neo4j Connection
# -----------------------------
URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# -----------------------------
# File paths
# -----------------------------
PERSONS_FILE = "data/persons.csv"


# -----------------------------
# Create Person Nodes
# -----------------------------
def create_persons(tx, person):
    tx.run(
        """
        MERGE (p:Person {person_id: $person_id})
        SET p.name = $name,
            p.age = $age
        """,
        person_id=str(person["person_id"]),
        name=str(person["name"]),
        age=int(person["age"])
    )


# -----------------------------
# Main Function
# -----------------------------
def main():

    print("Reading persons.csv...")

    persons = pd.read_csv(PERSONS_FILE)

    print(f"Found {len(persons)} persons")

    with driver.session() as session:

        for _, person in persons.iterrows():
            session.execute_write(create_persons, person)

    print("Person nodes created successfully!")


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":

    try:
        main()

    except Exception as e:
        print("Error:", e)

    finally:
        driver.close()