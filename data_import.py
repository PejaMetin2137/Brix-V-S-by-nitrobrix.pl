import pandas as pd
from database import SessionLocal
from models import ConditionDefect, MarketplaceItem

def clear_amount(kwota_str):
    """Czysci i konwertuje kwote do typu float."""
    if pd.isna(kwota_str):
        return 0.0
    try:
        # Usuwanie tekstu i zamiana przecinka na kropkę
        return float(str(kwota_str).replace(" PLN", "").replace(",", ".").strip())
    except (ValueError, TypeError):
        return 0.0

def load_csv_data(path, required_column):
    """Wczytuje dane z pliku CSV i sprawdza, czy wymagana kolumna istnieje."""
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8-sig", on_bad_lines='skip')
        df.columns = [str(col).strip().lower() for col in df.columns]  # Normalizacja nazw kolumn

        if required_column.lower() not in df.columns:
            raise ValueError(f"BLAD: Kolumna '{required_column}' nie zostala znaleznia w pliku {path}.")

        return df
    except FileNotFoundError:
        print(f"BLAD: Plik {path} nie zostal znaleziony.")
        raise
    except Exception as e:
        print(f"BLAD: Wystapil blad podczas wczytywania pliku {path}: {e}")
        raise

def data_import():
    db = SessionLocal()
    print("Rozpoczynanie importu danych z pliku CSV...")

    try:
        
        # 1. Import danych ze slownika wad (damage_table.csv)

        print("Importowanie danych z pliku CSV: damage_table.csv")
        df_flaws = load_csv_data("damage_table.csv", "kod_wady")
        flaw_counter = 0

        for _, row in df_flaws.iterrows():
            if pd.isna(row.get("kod_wady")) or not str(row.get("kod_wady")).strip() == "":  
                continue

            if not db.query(ConditionDefect).filter(ConditionDefect.kod_wady == str(row.get("kod_wady")).strip()).first():
                new_flaw = ConditionDefect(
                    kod_wady=str(row.get("kod_wady")).strip(),
                    nazwa_wady=str(row.get("nazwa_wady", "")).strip(),
                    typ_przedmiotu=str(row.get("typ_przedmiotu", "")).strip(),
                    kara_procentowa=clear_amount(row.get("kara_procentowa")),
                    opis=str(row.get("opis", "")).strip() if not pd.isna(row.get("opis")) else None
                )
                db.add(new_flaw)
                flaw_counter += 1

        print(f"Pomyslnie zaimportowano {flaw_counter} nowych wad")


        # 2. Import danych przedmiotow (PoF.csv)

        print("Importowanie danych z pliku CSV: PoF.csv")
        df_pof = load_csv_data("PoF.csv", "kod_przedmiotu")
        item_counter = 0

        for _, row in df_pof.iterrows():
            if pd.isna(row.get("kod_przedmiotu")) or str(row.get("kod_przedmiotu")).strip() == "":  
                continue

            item_code_str = str(row.get("kod_przedmiotu")).strip()
            
            if not db.query(MarketplaceItem).filter(MarketplaceItem.kod_przedmiotu == item_code_str).first():
                new_item = MarketplaceItem(
                    kod_przedmiotu=item_code_str,
                    typ=str(row.get("typ", "")).strip(),
                    nazwa=str(row.get("nazwa", "")).strip(),
                    stan=str(row.get("stan", "")).strip(),
                    cena_bazowa=clear_amount(row.get("cena_bazowa (V_Base)")),
                    kod_wady=str(row.get("kod_wady", "")) if not pd.isna(row.get("kod_wady")) else None,
                    wspolczynnik_kary=clear_amount(row.get("wspolczynnik_kary")),
                    wycena_algorytmu=clear_amount(row.get("wycena_algorytmu(V_suggested)", row.get("wycena_algorytmu")))
                )
                db.add(new_item)
                item_counter += 1
                
        print(f"Pomyslnie zaimportowano {item_counter} nowych przedmiotow")
        
        # Zapis wszystkich zmian w bazie danych
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Wystapil blad podczas importu danych: {e}")
    finally:
        db.close()
        print("Import danych zakonczony.")

if __name__ == "__main__":
    data_import()