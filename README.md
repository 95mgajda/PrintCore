# PrintCore – Baza danych do obsługi klientów / Customer Database Project

##  Opis projektu / Project Description

PrintCore to projekt bazy danych przygotowany w ramach studiów podyplomowych BIG DATA.

Celem projektu jest stworzenie systemu obsługi klientów, zamówień i produktów z użyciem SQL Server Management Studio (SSMS).

---

PrintCore_DB is a database project prepared as part of postgraduate BIG DATA studies.

The goal of the project is to build a customer, order, and product management system using SQL Server Management Studio (SSMS).

---

## 🛠 Technologie / Technologies

- SQL Server Management Studio (SSMS)
- SQL

---

##  Pliki w repozytorium / Files in the repository

- `printcore_db.sql` – kod do utworzenia bazy danych i wstawienia danych testowych 
  SQL script to create the database and insert test data

- `printcore_erd.pdf` – diagram relacji (ERD)  
  Entity-relationship diagram (ERD)

- `README.md` – opis projektu  
  Project description

✅ Daily commit 2025-07-10: mała zmiana dla utrzymania ciągłości pracy.

## Orders data generator 2025-07-22:

- Script: `generate_orders.py`
- Description: Generates fake orders with random client, date, and amount.
- Requirements: pandas, pyodbc, faker

## Raportowanie
Skrypt `generate_raport.py` generuje plik CSV z podsumowaniem zamówień na klienta (liczba zamówień, łączna wartość).


## Scripts
- `generate_products.py` – losowe generowanie produktów do bazy (30 wpisów)
- `generate_raport.py` generuje plik CSV z podsumowaniem zamówień na klienta (liczba zamówień, łączna wartość).
---

## 👤 Autor / Author

Maciej Gajda

---

## 💡 Dodatkowe informacje / Additional Info

Projekt demonstracyjny do nauki SQL, ETL i modelowania danych.  
Demonstration project for learning SQL, ETL, and data modeling.

## Import danych

- Python script: `import_clients.py`  
- Dependencies: pandas, pyodbc  
- Tested on: SQL Server LocalDB, database PrintCore_Test, table Clients_Test



