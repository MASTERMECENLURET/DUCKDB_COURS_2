from concurrent.futures import ThreadPoolExecutor
import duckdb

def update_data(thread_id):
    new_name = f"George ({thread_id})"
    with duckdb.connect("presidents.duckdb") as conn:
        print(f"Thread {thread_id} starting its update.")
        conn.sql(
            f"""
            UPDATE presidents
            SET first_name = '{new_name}'
            WHERE sequence = 1
            """
        )
        print(f"Thread {thread_id} ending its update.")


def concurrent_update():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(update_data, range(3))

concurrent_update()