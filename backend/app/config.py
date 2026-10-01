from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@127.0.0.1:5432/medidemo"
    secret_key: str = "526a7d62268f1fa98965eb73389b61350c31e547edcfd19d208742102e0940fa"
    frontend_origin: str = "https://localhost:5173"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()