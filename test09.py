import duckdb

with duckdb.connect("presidents.duckdb") as conn:
    result = conn.sql(
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