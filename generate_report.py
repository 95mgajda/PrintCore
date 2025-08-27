import pandas as pd

# Wczytanie danych
df = pd.read_csv('../data/clients_for_sql.csv')

# Policz liczbę klientów wg typu
client_counts = df['Client_Type'].value_counts()

# Policz liczbę unikalnych emaili
unique_emails = df['Email'].nunique()

# Zapisz wyniki do pliku
with open('../data/report.txt', 'w', encoding='utf-8') as f:
    f.write('Client Type Counts:\n')
    f.write(client_counts.to_string())
    f.write('\n\nUnique Emails Count:\n')
    f.write(str(unique_emails))

print("Report generated: report.txt")
