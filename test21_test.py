import duckdb

def short_name(first_name: str, last_name: str) -> str:
    return f"{first_name[0]}. {last_name}"

duckdb.create_function("short_name", short_name)

presidents = duckdb.read_parquet("presidents.parquet")

duckdb.sql(
    """
    SELECT short_name(first_name, last_name) AS name,
    (term_end - term_start) AS days_in_office
    FROM presidents
    """
).limit(3).show()