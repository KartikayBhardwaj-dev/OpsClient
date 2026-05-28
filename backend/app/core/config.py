# ------CREATING THIS TO INITALIZE POSTGRESQL REDIS CHROMA SETUP-------
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "OpsClient"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    GROQ_API_KEY: str
    DATABASE_URL: str
    REDIS_URL: str
    CHROMA_DB_PATH: str = "./chroma_db"
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()