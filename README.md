# Brix-V&S-by-nitrobrix.pl, czyli system wspomagania wyceny i obrotu kolekcjonerskimi zestawami, minifigurkami oraz przedmiotami powiązanymi z LEGO Star Wars

Projekt realizowany w ramach inżynierskiej pracy dyplomowej.
Aplikacja webowa służąca do automatycznej wyceny wartości używanych i nowych zestawów oraz minifigurek (z uwzględnieniem wad fizycznych oraz kompletności) na podstawie danych rynkowych, z możliwym wbudowanym modułem marketplace.

# Stack technologiczny
  - **Baza danych:** PostgreSQL (relacyjna) + Redis (cache)  
  - **Środowisko:** Docker / docker-compose
  - **Backend:** tb
  - **Frontend:** tb

# Uruchomienie środowiska lokalnego
```bash
docker-compose up -d
