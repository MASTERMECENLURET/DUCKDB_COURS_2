import duckdb

def short_name(first_name: str, last_name: str) -> str:
    return f"{first_name[0]}. {last_name}"