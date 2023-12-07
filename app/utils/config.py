from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()
class Settings(BaseSettings):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()