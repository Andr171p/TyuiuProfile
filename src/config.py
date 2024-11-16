from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class DBSettings(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str


class Settings(BaseSettings):
    db: DBSettings = DBSettings()


settings = Settings()
