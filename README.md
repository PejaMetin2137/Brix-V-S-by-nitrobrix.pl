# Brix-V&S-by-nitrobrix.pl
System wspomagania wyceny i obrotu kolekcjonerskimi zestawami, minifigurkami oraz przedmiotami powiązanymi z LEGO Star Wars.

Projekt realizowany w ramach inżynierskiej pracy dyplomowej.
Aplikacja webowa służąca do automatycznej wyceny wartości używanych i nowych zestawów oraz minifigurek (z uwzględnieniem wad fizycznych oraz kompletności) na podstawie danych rynkowych, z możliwym wbudowanym modułem marketplace.

## Struktura plików
 - **database.py:** odpowiada za konfigurację połączenia z bazą danych oraz zarządzanie sesją ('SessionLocal').
 - **models.py:** odpowiada za definicja tabel w bazie danych (np. 'ConditionDefect', 'MarketplaceItems'), wykorzystujące SQLAlchemy.
 - **data_import.py:** skrypt ETL, wczytujący dane z plików CSV, oczyszcza je (parsowanie kwot walutowych) i zapisuje w bazie, ignorując duplikaty.

## Formatowanie plików CSV
Skrypt **data_import.py** wymaga dokładnie sformatowanych plików wejściowych: 'damage_table.csv' oraz 'PoF.csv'.
Wymagane ustawienia:
  - **Eksport pliku jako .csv.**
  - **Kodowanie:** UTF-8.
  - **Separator:** Średnik.

## Uruchomienie środowiska lokalnego
```bash
docker-compose up -d
python3 -m venv venv
source venv/bin/activate
```

## Start aplikacji
```bash
uvicorn main:app --reload
```

## Uruchamianie importu
```bash
python data_import.py
```

