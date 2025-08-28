from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "ZenLTD Backend"
    DATABASE_URL: str  # Directly load from .env

    class Config:
        env_file = ".env"

settings = Settings()
