from fastapi import FastAPI
from database import engine, Base
import models

# Tworzenie tabel w bazie danych na podstawie modeli
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LEGO Star Wars Pricing API",
    description="API do wyceny przedmiotów LEGO Star Wars na podstawie ich stanu i ewentualnych wad.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status":"ok", "message":"Server is running, tables have been created successfully."}
