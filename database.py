from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#URL do łączenia z bazą danych PostgreSQL w Dockerze
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://admin:secretpassword@localhost:5432/lego_db"

# Tworzenie silnika bazy danych
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#Konfiguracja sesji bazy danych dla zapytań
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Klasa bazowa dla modeli
Base = declarative_base()

