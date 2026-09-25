import duckdb

result = duckdb.sql("SELECT 'whistling_duck' AS waterfowl, 'whistle' AS call")

print(result)