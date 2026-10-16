from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    driver.verify_connectivity()
    print("Neo4j Connected Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (p:Person) RETURN count(p) AS total"
        )
        total = result.single()["total"]

        print("Total Persons in Database:", total)

finally:
    driver.close()