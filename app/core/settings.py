from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    APP_VERSION: str = "1.0"
    APP_NAME: str
    APP_DESCRIPTION: str = None
    APP_DEBUG: bool = False
    APP_SWAGGER_URL: str = None
    APP_REDOC_URL: str = None
    FAISS_VECTOR_DIMENSION: int = 384
    CHUNK_LIMIT: int = 300
    CHUNK_OVERLAP_LIMIT: int = 50
    LLM_MODEL_NAME: str = "google/flan-t5-small"
    DEVICE_MAP:str = "auto"
    MAX_NEW_TOKENS:int = 300
    TEMPERATURE:float = 0.3
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()