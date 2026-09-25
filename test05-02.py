import duckdb


with duckdb.connect(database="presidents.duckdb") as conn:
    result = conn.sql("SELECT * FROM presidents_relation")
    print(result)
