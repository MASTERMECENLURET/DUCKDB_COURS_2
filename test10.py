import duckdb

presidents = duckdb.read_parquet("presidents.parquet")
parties = duckdb.read_json("parties.json")

result = duckdb.sql(
    """
    SELECT first_name, last_name, party_name
    FROM presidents
    JOIN parties
    ON presidents.party_id = parties.party_id
    WHERE party_name = 'Whig'
    ORDER BY last_name DESC
    """
)

print(result)