import pandas as pd
import pyodbc

# === 1. CONFIGURATION ===
# Ścieżka do pliku CSV z danymi klientów
csv_file = r'D:\GG Draft\BigData\PrintCore\data\clients_for_sql.csv'

# Ustawienia połączenia z bazą danych
server = r'(localdb)\localDB1'
database = 'PrintCore'
table = 'dbo.Clients'

# === 2. EXTRACT ===
# Wczytywanie danych z CSV do DataFrame (czyli tabeli pandas)
df = pd.read_csv(csv_file)

# Usuń kolumnę Client_ID jeśli istnieje (bo w bazie generuje się automatycznie)
if 'Client_ID' in df.columns:
    df = df.drop(columns=['Client_ID'])

# Konwersja kolumn NIP i Phone na string (dla bezpieczeństwa INSERTU)
df['NIP'] = df['NIP'].astype(str)
df['Phone'] = df['Phone'].astype(str)

# === 3. CONNECT TO DATABASE ===
# Łączenie z bazą danych przez pyodbc
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# === 4. LOAD DATA ===
# Iteracja po wybranych kolumnach
for index, row in df[['First_Name', 'Last_Name', 'Email', 'Phone', 'NIP', 'Client_Type']].iterrows():
    print(f"Inserting row: {row.to_dict()}")  # logujemy wiersz
    cursor.execute(
        f"INSERT INTO {table} (First_Name, Last_Name, Email, Phone, NIP, Client_Type) VALUES (?, ?, ?, ?, ?, ?)",
        row['First_Name'],
        row['Last_Name'],
        row['Email'],
        row['Phone'],
        row['NIP'],
        row['Client_Type'],
    )

# Zatwierdzanie zmian w bazie
conn.commit()

# === 5. CLEANUP ===
cursor.close()
conn.close()

print("Import completed successfully!")
