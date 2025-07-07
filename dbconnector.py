import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="LostandFound",
    user="postgres",
    password="the1975isgood"
)

print("Connection successful!")