import pandas as pd
import pyodbc

# Ścieżka do pliku CSV z danymi testowymi
csv_file = r'D:\GG Draft\BigData\PrintCore\data\clients_test.csv'

# Ustawienia połączenia z nową bazą
server = r'(localdb)\localDB1'
database = 'PrintCore_Test'
table = 'dbo.Clients_Test'

# EXTRACT
df = pd.read_csv(csv_file)

# Usuń Client_ID jeśli jest
if 'Client_ID' in df.columns:
    df = df.drop(columns=['Client_ID'])

# Rzutowanie typów
df['NIP'] = df['NIP'].astype(str)
df['Phone'] = df['Phone'].astype(str)

# CONNECT
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# LOAD
for index, row in df[['First_Name', 'Last_Name', 'Email', 'Phone', 'NIP', 'Client_Type']].iterrows():
    print(f"Inserting row: {row.to_dict()}")
    cursor.execute(
        f"INSERT INTO {table} (First_Name, Last_Name, Email, Phone, NIP, Client_Type) VALUES (?, ?, ?, ?, ?, ?)",
        row['First_Name'],
        row['Last_Name'],
        row['Email'],
        row['Phone'],
        row['NIP'],
        row['Client_Type'],
    )

# Commit + Cleanup
conn.commit()
cursor.close()
conn.close()

print("Import completed successfully!")
