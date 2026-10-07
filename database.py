from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# URL do laczenia z baza danych PostgreSQL w Dockerze
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:secretpassword@localhost:5432/lego_db"

# Tworzenie silnika bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Konfiguracja sesji bazy danych dla zapytan
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Klasa bazowa dla modeli
Base = declarative_base()

