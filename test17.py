import duckdb

with duckdb.connect("presidents.duckdb") as conn:
    result = conn.sql(
        """
        SELECT last_name, first_name
        FROM presidents
        WHERE sequence = 1
        """
    )
    result.show()