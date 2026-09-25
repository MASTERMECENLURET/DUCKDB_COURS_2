import duckdb

conn = duckdb.connect(database="presidents.duckdb")
presidents_relation = conn.read_parquet("presidents.parquet")
result = conn.sql(
    """
    SELECT sequence, last_name, first_name
    FROM presidents_relation
    WHERE sequence <= 2
    """
)
print(result)
#result.show()
presidents_relation.to_table("presidents") 
conn.close()