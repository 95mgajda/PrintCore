import pyodbc
import random

# === 1. CONFIG ===
server = r'(localdb)\localDB1'
database = 'PrintCore_Test'
table = 'dbo.Products'

# Lista przykładowych nazw i kategorii
product_names = [
    "Filament PLA", "Filament PETG", "Filament ABS", "Resin UV", "Nozzle 0.4mm",
    "Nozzle 0.6mm", "Platform Tape", "Build Plate", "Motor NEMA17", "Heated Bed"
]

categories = [
    "Materiały", "Akcesoria", "Części", "Chemia", "Mechanika"
]

# === 2. CONNECT TO DATABASE ===
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# === 3. GENERATE & INSERT ===
num_products = 30

for _ in range(num_products):
    name = random.choice(product_names)
    category = random.choice(categories)
    price = round(random.uniform(10.0, 500.0), 2)

    print(f"Inserting: {name} ({category}) - {price} PLN")

    cursor.execute(
        f"INSERT INTO {table} (Product_Name, Category, Price) VALUES (?, ?, ?)",
        name, category, price
    )

# === 4. COMMIT & CLOSE ===
conn.commit()
cursor.close()
conn.close()

print("Products generated and inserted successfully.")
