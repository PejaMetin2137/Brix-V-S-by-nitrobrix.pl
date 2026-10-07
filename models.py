from sqlalchemy import Column, Integer, String, Float, Text
from database import Base

class ConditionDefect(Base):
    __tablename__ = "slownik_wad"

    id = Column(Integer, primary_key=True, index=True)
    kod_wady = Column(String(50), unique=True, index=True, nullable=False)
    nazwa_wady = Column(String(100), nullable=False)
    typ_przedmiotu = Column(String(20), nullable=False)
    kara_procentowa = Column(Float, nullable=False)
    opis = Column(Text, nullable=True)

class MarketplaceItem(Base):
    __tablename__ = "przedmioty"

    id = Column(Integer, primary_key=True, index=True)
    kod_przedmiotu = Column(String(50), index=True, nullable=False)
    typ = Column(String(20), nullable=False)
    nazwa = Column(String(150), nullable=False)
    stan = Column(String(20), nullable=False)
    cena_bazowa = Column(Float, nullable=False)
    kod_wady = Column(String(100), nullable=True)
    wspolczynnik_kary = Column(Float, default=0.0)
    wycena_algorytmu = Column(Float, nullable=False)
