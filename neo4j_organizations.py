import pandas as pd
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

df = pd.read_csv("data/organizations.csv")

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
                MERGE (o:Organization {
                    organization_id: $organization_id
                })
                SET o.organization_name = $organization_name
                MERGE (p)-[:ASSOCIATED_WITH]->(o)
                """,
                person_id=row["person_id"],
                organization_id=row["organization_id"],
                organization_name=row["organization_name"]
            )

    print("Organization Nodes and Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (o:Organization) RETURN count(o) AS total"
        )
        print("Total Organizations:", result.single()["total"])

finally:
    driver.close()
