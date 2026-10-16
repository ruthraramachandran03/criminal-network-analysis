import pandas as pd
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

df = pd.read_csv("data/locations.csv")

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
                MERGE (l:Location {location_id: $location_id})
                SET l.location_name = $location_name
                MERGE (p)-[:VISITED]->(l)
                """,
                person_id=row["person_id"],
                location_id=row["location_id"],
                location_name=row["location_name"]
            )

    print("Location Nodes and Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (l:Location) RETURN count(l) AS total"
        )
        print("Total Locations:", result.single()["total"])

finally:
    driver.close()
