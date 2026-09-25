#uv add pyarrow polars
import duckdb

presidents = duckdb.read_parquet("presidents.parquet").set_alias(
    "presidents"
)
parties = duckdb.read_json("parties.json").set_alias("parties")

result = (
    presidents.join(parties, "presidents.party_id = parties.party_id")
    .select("first_name", "last_name", "party_name")
    .order("last_name DESC")
).pl().head(3)

print(result)