#CHANGELOG

## [v0.1.0] - 10-07-2025
### Added
-Initial SQL data base structure
- README file

## [v0.2.0] - 11-07-2025
- Sample Python script for generating test data

- Example SQL queries

- # 📝 CHANGELOG

Wszystkie istotne zmiany i dodatki w projekcie PrintCore.

## [v0.3.0] - 12-07-2025
### Dodano
- `import_clients.py` – skrypt ETL importujący dane klientów z pliku `.csv` do bazy SQL Server (`Clients_Test`)
- `generate_order.py` – skrypt do generowania zamówień z użyciem `faker` i przypisywania ich do istniejących klientów
- `generate_product_report_excel.py` – raport podsumowujący zamówienia na produkty, eksportowany do Excela
- `generate_raport.py` – raport podsumowujący klientów i łączną wartość ich zamówień, eksportowany do `.csv`
- `import_products.py` – import danych o produktach do tabeli `Products`
- `import_order_details.py` – automatyczne generowanie i zapis danych do tabeli `OrderDetails`
- `requirements.txt` – aktualizacja zależności (`pandas`, `faker`, `pyodbc`, `openpyxl`)
- `clients_for_sql.csv` – testowy plik z wygenerowanymi danymi klientów

### Poprawki
- Refaktoryzacja ścieżek do plików
- Usunięcie błędów z połączeniami do baz danych
- Obsługa typów danych (np. konwersja NIP/Phone na string)

---

## [v0.4.0] - 13-08-2025
### Dodano
- `generate_full_report_excel.py` – raport zawierający wiele arkuszy (Info, Klienci, Produkty)

