import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

# Connect to your postgres DB
conn = psycopg2.connect(
    host=os.getenv("SQL_HOST"),
    user=os.getenv("SQL_USER"),
    password=os.getenv("SQL_PASS")
    )

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
cur.execute(
    "INSERT INTO test (num, data) VALUES (%s, %s)",
    (101, "abc'defg")
    )
cur.execute("SELECT * FROM test;")

# Retrieve query results
records = cur.fetchall()

conn.commit()

cur.close()
conn.close()