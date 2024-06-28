import os
from pathlib import Path
from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    BASE_DIR = Path(__file__).resolve().parent.parent

    @property
    def WRITER_DB_URL(self):
        WDB_URL = f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        print(WDB_URL)
        return WDB_URL
    @property
    def READER_DB_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env.dev"


env = Config()