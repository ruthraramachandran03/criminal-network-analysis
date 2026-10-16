import pandas as pd
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

df = pd.read_csv("data/vehicles.csv")

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
                MERGE (v:Vehicle {vehicle_id: $vehicle_id})
                SET v.vehicle_number = $vehicle_number
                MERGE (p)-[:USES_VEHICLE]->(v)
                """,
                person_id=row["person_id"],
                vehicle_id=row["vehicle_id"],
                vehicle_number=str(row["vehicle_number"])
            )

    print("Vehicle Nodes and Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (v:Vehicle) RETURN count(v) AS total"
        )
        print("Total Vehicles:", result.single()["total"])

finally:
    driver.close()
