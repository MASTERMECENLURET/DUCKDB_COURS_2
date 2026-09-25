import duckdb

with duckdb.connect(database="presidents.duckdb") as conn:
    result = conn.sql(
        """
        SELECT last_name, first_name
        FROM presidents
        WHERE last_name = 'Adams'
        """
    )
    print(result)