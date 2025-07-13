# Importujemy bibliotekę pandas, która służy do pracy z danymi tabelarycznymi (np. CSV)
import pandas as pd

# === EXTRACT (EKSTRAKCJA) ===
# Wczytujemy dane z pliku CSV do obiektu DataFrame (czyli takiej tabeli w pamięci Pythona)
# Ścieżka '../data/clients_for_sql.csv' oznacza: wyżej o jeden folder, potem do folderu data
df = pd.read_csv('../data/clients_for_sql.csv')

# === TRANSFORM (TRANSFORMACJA) ===
# Z całej tabeli wybieramy tylko kolumny 'First_Name' i 'Last_Name'
# apply(lambda x: x.str.upper()) sprawia, że wszystkie wartości w tych kolumnach zmienią się na DUŻE LITERY
df_transformed = df[['First_Name', 'Last_Name']].apply(lambda x: x.str.upper())

# === LOAD (ZAŁADOWANIE) ===
# Zapisujemy przetworzone dane do nowego pliku CSV
# index=False oznacza: nie zapisuj numerów wierszy (indeksów) do pliku
df_transformed.to_csv('../data/clients_transformed.csv', index=False)

# Na koniec informujemy użytkownika, że ETL się zakończył
print("ETL completed: clients_transformed.csv created!")