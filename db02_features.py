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
        print(f"[\u2713] Executed SQL file: {sql_file_path.name}")
    except FileNotFoundError:
        print(f"[!] SQL file not found: {sql_file_path.name}")
    except Exception as e:
        print(f"[!] Error executing SQL file ({sql_file_path.name}): {e}")

def main():
    # Define paths
    root_dir = pathlib.Path(__file__).parent.resolve()
    data_folder = root_dir / "data"
    sql_folder = root_dir / "sql_features"
    db_path = data_folder / "project.sqlite3"

    # Connect to database
    try:
        conn = sqlite3.connect(db_path)
        print(f"[\u2713] Connected to database: {db_path.name}")

        # Execute SQL feature scripts (update/delete/select/etc.)
        execute_sql_file(conn, sql_folder / "delete_records.sql")
        execute_sql_file(conn, sql_folder / "update_records.sql")
    

        print("[\u2713] Feature queries executed successfully.")
    except Exception as e:
        print(f"[!] Database feature execution failed: {e}")
    finally:
        conn.close()
        print("[\u2713] Database connection closed.")

if __name__ == "__main__":
    main()
