import pandas as pd
from neo4j import GraphDatabase

# Neo4j connection details
URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

# Read persons data from CSV
df = pd.read_csv("data/persons.csv")

# Connect to Neo4j
driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

print("Creating Person Nodes...")

try:
    with driver.session() as session:

        for _, row in df.iterrows():

            session.run(
                """
                MERGE (p:Person {person_id: $person_id})
                SET p.name = $name,
                    p.age = $age
                """,
                person_id=row["person_id"],
                name=row["name"],
                age=int(row["age"])
            )

        print("All Person Nodes Created Successfully!")

        result = session.run(
            "MATCH (p:Person) RETURN count(p) AS total"
        )

        total = result.single()["total"]

        print("Total Persons in Database:", total)

finally:
    driver.close()