import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    user = "",
    database = "",
    password = "",
    port = 5432 
)

cur = conn.cursor()
cur.execute("""CREATE TABLE task
(id SERIAL PRIMARY KEY,
name VARCHAR(50) UNIQUE NOT NULL, 
isACtive BOOLEAN DEFAULT NOT TRUE ); 
""")

conn.commit()

fetch_query = "SELECT * FROM task WHERE isActive = TRUE;"
    cur.execute(fetch_query)
    active_tasks = cur.fetchall()
    print(f"Number of active tasks: {len(active_tasks)}")

cur.close()
conn.close()
