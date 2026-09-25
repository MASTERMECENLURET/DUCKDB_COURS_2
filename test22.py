import duckdb

with duckdb.connect("presidents.duckdb") as conn:
    pandas_presidents = conn.sql(
        """
        SELECT last_name, first_name
        FROM presidents
        WHERE sequence BETWEEN 2 AND 5
        """
    ).df()

print(pandas_presidents)