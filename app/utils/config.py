from os import path, environ
from pydantic import BaseSettings
from dataclasses import dataclass

workspace = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


class Config(BaseSettings):
    DEBUG: bool = True
    BASE_DIR = workspace

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


class LocalConfig(Config):
    PROJ_RELOAD: bool = True


