import csv
from faker import Faker
import random

#Tworzymy generator Faker
fake = Faker('pl_PL') #Polskie dane

#Ilość rekordów do wygenerowania
NUM_RECORDS = 100

#Plik wynikowy

OUTPUT_FILE = ('clients_for_sql.csv')

#Nagłówki kolumn
headers = ['Client_ID', 'First_Name', 'Last_Name', 'Email', 'Phone', 'NIP', 'Client_Type']

client_types = ['B2B', 'B2C']

#Generujemy dane
with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for i in range(1, NUM_RECORDS + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        nip = fake.random_number(digits=10, fix_len=True)
        client_type = random.choice(client_types)

        writer.writerow([i, first_name, last_name, email, phone, nip, client_type])

print(f"Wygenerowano {NUM_RECORDS} rekordów w pliku {OUTPUT_FILE}")