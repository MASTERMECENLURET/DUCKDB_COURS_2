from concurrent.futures import ThreadPoolExecutor
import duckdb

def read_data(thread_id):
    print(f"Thread {thread_id} starting its read.")
    with duckdb.connect("presidents.duckdb") as conn:
        conn.sql(
            """
            SELECT first_name, last_name
            FROM presidents
            WHERE sequence = 1
            """
        ).show()
    print(f"Thread {thread_id} ending its read.")


def concurrent_read():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(read_data, range(3))

concurrent_read()