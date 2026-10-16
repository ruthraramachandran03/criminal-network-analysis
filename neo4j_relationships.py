from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# Sample relationships between persons
relationships = [
    ("P001", "P003"),
    ("P002", "P003"),
    ("P002", "P004"),
    ("P004", "P005"),
    ("P005", "P006"),
    ("P006", "P007"),
    ("P007", "P008")
]

try:
    with driver.session() as session:

        for person1, person2 in relationships:
            session.run(
                """
                MATCH (a:Person {person_id: $id1})
                MATCH (b:Person {person_id: $id2})
                MERGE (a)-[:CONNECTED_TO]->(b)
                """,
                id1=person1,
                id2=person2
            )

    print("Person Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            """
            MATCH (:Person)-[r:CONNECTED_TO]->(:Person)
            RETURN count(r) AS total
            """
        )

        print("Total Relationships:", result.single()["total"])

finally:
    driver.close()
