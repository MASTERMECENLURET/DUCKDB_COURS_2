import duckdb

leaders = duckdb.read_parquet("presidents.parquet").set_alias(
    "usa_presidents"
)
faction = duckdb.read_json("parties.json").set_alias("political_parties")

(
    leaders
    .join(faction, "usa_presidents.party_id = political_parties.party_id")
    .select("first_name", "last_name", "party_name")
    .filter("party_name = 'Whig'")
    .order("last_name DESC")
    .show()
)