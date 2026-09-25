import duckdb

presidents = duckdb.read_parquet("presidents.parquet")

duckdb.sql(
    """
    SELECT short_name(first_name, last_name) AS name,
    (term_end - term_start) AS days_in_office
    FROM presidents
    """
).limit(3)