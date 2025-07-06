import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=2454,
    dbname="LostandFound",
    user="postgres",
    password="the1975isgood"
)

print("Connection successful!")