import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    team_id: str = ""
    backend_api: str = "https://aes-agniachallenge-case.olymp.innopolis.university/"
    root_directory: str = os.path.dirname(__file__)


settings = Settings()
