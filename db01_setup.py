import sqlite3
import pathlib

def execute_sql_file(conn, sql_file_path):
    """
    Executes all SQL commands in the given file using the provided connection.
    """
    try:
        with open(sql_file_path, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"[✓] Executed SQL file: {sql_file_path}")
    except FileNotFoundError:
        print(f"[!] SQL file not found: {sql_file_path}")
    except Exception as e:
        print(f"[!] Error executing SQL file ({sql_file_path}): {e}")

def main():
    # Define paths
    root_dir = pathlib.Path(__file__).parent.resolve()
    data_folder = root_dir / "data"
    sql_folder = root_dir / "sql_create"
    db_path = data_folder / "project.sqlite3"

    # Create data folder if it doesn't exist
    data_folder.mkdir(exist_ok=True)

    # Connect to database (it will be created if it doesn't exist)
    try:
        conn = sqlite3.connect(db_path)
        print(f"[✓] Connected to database: {db_path}")

        # Run SQL scripts (optional: comment out if not needed)
        execute_sql_file(conn, sql_folder / "01_drop_tables.sql")
        execute_sql_file(conn, sql_folder / "02_create_tables.sql")
        execute_sql_file(conn, sql_folder / "03_insert_records.sql")

        print("[✓] Database setup completed successfully.")
    except Exception as e:
        print(f"[!] Database setup failed: {e}")
    finally:
        conn.close()
        print("[✓] Database connection closed.")

if __name__ == "__main__":
    main()
