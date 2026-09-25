import duckdb

with duckdb.connect(database="presidents.duckdb") as conn:
    conn.read_json("parties.json").to_table("parties")