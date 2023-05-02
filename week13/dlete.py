import psycopg2
import csv

conn = psycopg2.connect(
    host = "localhost",
    database = "phonebook",
    user = "postgres",
    password = "Nurkhan05"
)
cur = conn.cursor()
name = input()
def delete_data(name=None):
    if name:
        cur.execute("DELETE FROM snake WHERE name=%s", (name,))
    conn.commit()
    print("We succesfull delete this contact")
delete_data(name=name)