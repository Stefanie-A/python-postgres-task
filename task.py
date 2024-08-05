import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv("host"),
        user=os.getenv("username"),
        database=os.getenv("database"),
        password=os.getenv("password"),
        port=os.getenv("port")
    )

    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS task (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL,
        isActive BOOLEAN DEFAULT FALSE
    );
    """)

    conn.commit()

    fetch_query = "SELECT * FROM task WHERE isActive = TRUE;"
    cur.execute(fetch_query)
    active_tasks = cur.fetchall()
    print(f"Number of active tasks: {len(active_tasks)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
