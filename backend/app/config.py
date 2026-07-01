from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    cors_origins: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()