import pandas as pd
from neo4j import GraphDatabase

URI = "neo4j://127.0.0.1:7687"
USERNAME = "neo4j"
PASSWORD = "Ruthra@0404"

df = pd.read_csv("data/transactions.csv")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

try:
    with driver.session() as session:
        for _, row in df.iterrows():
            session.run(
                """
                MATCH (sender:Person {person_id: $from_person})
                MATCH (receiver:Person {person_id: $to_person})

                MERGE (t:Transaction {
                    transaction_id: $transaction_id
                })

                SET t.amount = $amount,
                    t.transaction_type = $transaction_type

                MERGE (sender)-[:SENT]->(t)
                MERGE (t)-[:RECEIVED_BY]->(receiver)
                """,
                transaction_id=row["transaction_id"],
                from_person=row["from_person"],
                to_person=row["to_person"],
                amount=float(row["amount"]),
                transaction_type=row["transaction_type"]
            )

    print("Transaction Nodes and Relationships Created Successfully!")

    with driver.session() as session:
        result = session.run(
            "MATCH (t:Transaction) RETURN count(t) AS total"
        )
        print("Total Transactions:", result.single()["total"])

finally:
    driver.close()
