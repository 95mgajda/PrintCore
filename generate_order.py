import pandas as pd
import pyodbc
import random
from faker import Faker



# === 1.Configuration ===
server = r'(localdb)\localDB1'
database = 'PrintCore_Test'
orders_table = 'dbo.Orders'
clients_table = 'dbo.Clients_Test'

# === 2. Connect to Database ===
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# === 3. Prepare fake data ===
fake =  Faker()
num_orders = 50 #liczba zamowien do wygenerowania

# Pobierz liste istniejacych Client_ID z bazy

client_ids = []
cursor.execute(f"SELECT Client_ID FROM {clients_table}")
for row in cursor.fetchall():
    client_ids.append(row[0])

# Sprawdzenie, czy mamy w ogóle klientów

if not client_ids:
    raise Exception("Brak klientów w tabeli Clients_Test!")

# 4. Generate and inseret orders ===

for _ in range(num_orders):
    client_id = random.choice(client_ids) #losowy klient
    order_date = fake.date_between(start_date='-1y', end_date='today') #data z ostatniego roku
    order_amount = round(random.uniform(100.0, 10000.0), 2) #kwota 100-10 000 zł

    print(f"Inserting order: Client_ID = {client_id}, Date={order_date}, Amount={order_amount}")

    cursor.execute(
        f"INSERT INTO {orders_table} (Client_ID, Order_Date, Order_Amount) VALUES (?, ?, ?)",
        client_id,
        order_date,
        order_amount
    )

# === 5. Commit and Cleanup ===
conn.commit()
cursor.close()
conn.close()

print("Oders import completed sucessfully!")