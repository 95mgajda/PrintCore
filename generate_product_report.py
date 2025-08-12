import pyodbc
import pandas as pd

# === 1. CONFIG ===
server = r'(localdb)\localDB1'
database = 'PrintCore_Test'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

# === 2. CONNECT ===
conn = pyodbc.connect(conn_str)

# === 3. SQL QUERY ===
query = """
SELECT 
    p.Product_Name,
    p.Category,
    COUNT(od.OrderDetail_ID) AS Times_Ordered,
    SUM(od.Quantity) AS Total_Quantity,
    SUM(od.Total_Price) AS Total_Revenue
FROM dbo.OrderDetails od
JOIN dbo.Products p ON od.Product_ID = p.Product_ID
GROUP BY p.Product_Name, p.Category
ORDER BY Total_Quantity DESC;
"""

df = pd.read_sql(query, conn)

# === 4. EXPORT TO CSV ===
output_path = r"D:\GG Draft\BigData\PrintCore\output\product_summary.csv"
df.to_csv(output_path, index=False, sep=';', encoding='utf-8-sig')

print(f"✅ Report saved to {output_path}")

conn.close()
