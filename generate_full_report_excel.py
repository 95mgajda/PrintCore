import pandas as pd
from datetime import datetime

# === 1. Ścieżki ===
output_file = r"D:\GG Draft\BigData\PrintCore\output\full_report.xlsx"
clients_csv = r"D:\GG Draft\BigData\PrintCore\output\client_summary.csv"
products_excel = r"D:\GG Draft\BigData\PrintCore\output\product_summary.xlsx"

# === 2. Wczytanie danych ===
df_clients = pd.read_csv(clients_csv, sep=';')  # jeśli masz ; jako separator
df_products = pd.read_excel(products_excel)

# === 3. Arkusz z datą generacji ===
today = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
df_info = pd.DataFrame({
    "Informacja": ["Raport wygenerowany automatycznie"],
    "Data": [today]
})

# === 4. Zapis do Excela z wieloma arkuszami ===
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_info.to_excel(writer, sheet_name='Info', index=False)
    df_clients.to_excel(writer, sheet_name='Klienci', index=False)
    df_products.to_excel(writer, sheet_name='Produkty', index=False)

print(f"✅ Połączony raport Excel zapisany jako: {output_file}")
