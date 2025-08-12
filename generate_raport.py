import pandas as pd
import pyodbc


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

# === 3. SQL: Summary of orders per client ===

query = """
SELECT
    c.Client_ID,
    c.First_Name,
    c.Last_Name,
    c.Client_Type,
    COUNT(o.Order_ID) as Orders_Count,
    SUM(o.Order_Amount) as Total_Spent
    
From dbo.Clients_Test c
LEFT JOIN dbo.Orders o ON c.Client_ID = o.Client_ID
GROUP BY c.Client_ID, c.First_Name, c.Last_Name, c.Client_Type
ORDER BY Total_Spent DESC;
    
"""
df = pd.read_sql(query, conn)

# === 4. SAVE REPORT ===

output_path = r'D:\GG Draft\BigData\PrintCore\output\client_summary.csv'
df.to_csv(output_path, index=False, encoding='utf-8-sig', sep=';')

print(f" Report saved to {output_path}")

conn.close()