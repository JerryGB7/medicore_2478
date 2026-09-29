from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "https://localhost:5432/medidemo"
    secret_key: str 
    frontend_origin: str = "https://localhost:5173"
    model_config = SettingsConfigDict(env_file=".env")