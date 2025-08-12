import pyodbc
import random

# === 1. CONFIG ===
server = r'(localdb)\localDB1'
database = 'PrintCore_Test'
table = 'dbo.OrderDetails'

# === 2. CONNECT ===
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# === 3. GET existing Order_IDs and Product_IDs ===
cursor.execute("SELECT Order_ID FROM dbo.Orders")
order_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT Product_ID, Price FROM dbo.Products")
products = cursor.fetchall()  # list of tuples (Product_ID, Price)

# === 4. GENERATE OrderDetails ===
for order_id in order_ids:
    num_items = random.randint(1, 3)  # 1–3 items per order
    sampled_products = random.sample(products, num_items)

    for product_id, price in sampled_products:
        quantity = random.randint(1, 5)
        total_price = round(price * quantity, 2)

        print(f"Order {order_id}: {quantity}x Product {product_id} = {total_price} PLN")

        cursor.execute(
            f"""INSERT INTO {table} 
                (Order_ID, Product_ID, Quantity, Total_Price) 
                VALUES (?, ?, ?, ?)""",
            order_id, product_id, quantity, total_price
        )

# === 5. COMMIT & CLOSE ===
conn.commit()
cursor.close()
conn.close()

print("✅ OrderDetails generated and inserted successfully.")
