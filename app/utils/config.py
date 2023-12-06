from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URL: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()