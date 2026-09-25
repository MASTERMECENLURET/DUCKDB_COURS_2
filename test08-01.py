import duckdb

with duckdb.connect(database="presidents.duckdb") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS parties AS
        SELECT *
        FROM read_json_auto('parties.json')
    """)