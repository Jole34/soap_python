from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()

""""

Ova skripta se koristi za konfigurisanje (settings) iz .env fajla
koristeći Pydantic model. 

Pydantic omogućava definisanje tipova podataka i validaciju
kako bi se sve varijable iz env fajla dobile u pravom formatu.

load_dotenv() se koristi za ucitavanje vrednosti iz .env fajla u promenljive
kako bi Pydantic mogao da ih prepozna.

Config klasa u Settings klasi definiše dodatna podesavanja za Pydantic,
na primer, case_sensitive postavlja da su kljucevi u .env fajlu case-sensitive.

Instancu Settings klase (u ovom slucaju 'settings') koristimo kako bismo pristupili vrednostima podesavanja u nasoj aplikaciji.

"""""

class Settings(BaseSettings):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()