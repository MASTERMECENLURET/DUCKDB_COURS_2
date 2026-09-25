import duckdb

with duckdb.connect(database="presidents.duckdb") as conn:
    conn.execute("DROP TABLE IF EXISTS parties")
