import duckdb

with duckdb.connect(database="presidents.duckdb") as conn:
    presidents_relation = conn.read_csv("presidents.csv")
    result = presidents_relation.limit(2)
    print(result)