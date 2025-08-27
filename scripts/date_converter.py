import pandas as pd

# === 1. Wczytanie pliku ===
file_path = 'Holidays_PL_2025_2028.xlsx'   # <- zmień, jeśli plik nazywa się inaczej
sheet_name = 'Holidays_PL_2025_2028'       # <- sprawdź nazwę arkusza
df = pd.read_excel(file_path, sheet_name=sheet_name)

# === 2. Konwersja kolumny z datą ===
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')  # zamień tekst na datę
df["Formatted_Date"] = df["Date"].dt.strftime('%d.%m.%Y')  # nowy format

# === 3. Zapis do nowego pliku Excel ===
output_file = 'Holidays_Formatted.xlsx'
df.to_excel(output_file, index=False)

print(f"Gotowe! Plik zapisany jako: {output_file}")
