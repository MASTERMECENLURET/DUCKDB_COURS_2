# Attention  "uv add numpy pandas" pour que le script fonctionne
import duckdb

presidents = duckdb.read_parquet("presidents.parquet").set_alias(
    "presidents"
)
parties = duckdb.read_json("parties.json").set_alias("parties")

result = (
    presidents
    .join(parties, "presidents.party_id = parties.party_id")
    .select("first_name", "last_name", "party_name")
    .filter("party_name = 'Whig'")
    .order("last_name DESC")
    .fetchdf()
)

print(result)