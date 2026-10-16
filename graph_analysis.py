from neo4j import GraphDatabase
import networkx as nx

# Neo4j connection
URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# Create graph
G = nx.Graph()

print("Graph Analysis Started")

try:
    with driver.session() as session:

        # Get all persons
        result = session.run("""
            MATCH (p:Person)
            RETURN p.person_id AS person_id
        """)

        for record in result:
            G.add_node(record["person_id"])

        # Get person-to-person connections
        result = session.run("""
            MATCH (p1:Person)-[:CONNECTED_TO]-(p2:Person)
            RETURN DISTINCT
                p1.person_id AS person1,
                p2.person_id AS person2
        """)

        for record in result:
            G.add_edge(
                record["person1"],
                record["person2"]
            )

    # Count connections
    print("\nPerson Connections:")

    for person in sorted(G.nodes()):
        print(person, "->", G.degree(person))

    # Find the most connected person
    if G.number_of_nodes() > 0:
        most_connected = max(
            G.degree,
            key=lambda x: x[1]
        )

        print("\nMost Connected Person:")
        print(
            most_connected[0],
            "with",
            most_connected[1],
            "connections"
        )

    print("\nTotal Persons:", G.number_of_nodes())
    print("Total Connections:", G.number_of_edges())

    print("\nGraph Analysis Completed")

finally:
    driver.close()
