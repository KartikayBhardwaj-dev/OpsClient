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
    ENCRYPTION_KEY: str
    CHROMA_DB_PATH: str = "./chroma_db"
    GROQ_MODEL: str = "llama-3.1-8b-instant"
     # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    # Encryption
    ENCRYPTION_KEY: str
    # Google OAuth
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    GOOGLE_REDIRECT_URI: str

    SLACK_BOT_TOKEN: str
    SLACK_DEFAULT_CHANNEL: str
    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()