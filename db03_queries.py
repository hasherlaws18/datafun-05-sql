# Imports from Python Standard Library
import sqlite3
import pathlib

# Import local modules
from utils_logger import logger

def execute_sql_file(connection, file_path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.
    If the SQL is a SELECT query, prints the results to the terminal.
    """
    try:
        with open(file_path, 'r') as file:
            sql_script: str = file.read().strip()

        logger.info(f"Executing: {file_path.name}")

        # Check if it's a SELECT query
        if sql_script.lower().startswith("select"):
            cursor = connection.cursor()
            cursor.execute(sql_script)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            print(f"\n--- Results from: {file_path.name} ---")
            print(", ".join(columns))
            for row in rows:
                print(row)
            print("--- End of Results ---\n")
        else:
            connection.executescript(sql_script)

        logger.info(f"Executed successfully: {file_path.name}")

    except Exception as e:
        logger.error(f"Failed to execute {file_path.name}: {e}")
        raise

def main() -> None:
    logger.info("Starting query execution from sql_queries folder...")

    # Path setup
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_QUERIES_FOLDER = ROOT_DIR / "sql_queries"
    DATA_FOLDER = ROOT_DIR / "data"
    DB_PATH = DATA_FOLDER / "project.sqlite3"

    if not DB_PATH.exists():
        logger.error(f"Database file not found at {DB_PATH}. Run the setup script first.")
        return

    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        for sql_file in sorted(SQL_QUERIES_FOLDER.glob("*.sql")):
            execute_sql_file(connection, sql_file)

        logger.info("Query execution completed.")

    except Exception as e:
        logger.error(f"Query execution failed: {e}")

    finally:
        connection.close()
        logger.info("Database connection closed.")

if __name__ == '__main__':
    main()
