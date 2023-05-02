import psycopg2
import csv

conn = psycopg2.connect(
    host = "localhost",
    database = "phonebook",
    user = "postgres",
    password = "Nurkhan05"
)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(50) NOT NULL
)
''')

def insert_data_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader) # skip header row
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s)", (name, phone_number))
    conn.commit()

name = input()
phone_number = input()
def DataFromInput(name, phone_number):
    cur.execute("INSERT INTO phonebook(name, phone_number) VALUES(%s,%s)", (name, phone_number))
    conn.commit()
    print("this contact succesfull add in phonebook")

def update_data(name, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, name))
    if new_phone:
        cur.execute("UPDATE phonebook SET phone_number=%s WHERE name=%s", (new_phone, name))
    conn.commit()
    print("we change " + name + "'s data")

def query_data(name=None, phone=None):
    query = "SELECT * FROM phonebook"
    if name:
        query += " WHERE name=%s"
        cur.execute(query, (name,))
    elif phone:
        query += " WHERE phone=%s"
        cur.execute(query, (phone,))
    else:
        cur.execute(query)
    return cur.fetchall()

def delete_data(name=None, phone=None):
    if name:
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    elif phone:
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.commit()
    print("We succesfull delete this contact")

#insert_data_from_csv()#filepath #for inserting data into the phonebook from csv
#DataFromInput(name, phone_number) #for inserting data into the phonebook from consol
#update_data(name, new_phone = phone_number)#for changing data
results = query_data(name=name)#for showing data in consol
for result in results:
    print(result)
#delete_data(name = name, phone=phone_number)#for deletong data in tables
cur.close()
conn.close()
