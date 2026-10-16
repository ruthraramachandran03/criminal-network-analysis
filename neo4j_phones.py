import pandas as pd
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

df = pd.read_csv("data/phones.csv")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    with driver.session() as session:

        for _, row in df.iterrows():
            session.run(
                """
                MATCH (p:Person {person_id: $person_id})
                MERGE (ph:Phone {phone_id: $phone_id})
                SET ph.phone_number = $phone_number
                MERGE (p)-[:USES]->(ph)
                """,
                person_id=row["person_id"],
                phone_id=row["phone_id"],
                phone_number=str(row["phone_number"])
            )

    print("Phone Nodes and Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (ph:Phone) RETURN count(ph) AS total"
        )
        print("Total Phones:", result.single()["total"])

finally:
    driver.close()
