import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    team_id: str = "b051d03a-817d-4489-b198-f6b154a4c65f"
    backend_api: str = "https://aes-agniachallenge-case.olymp.innopolis.university/"
    root_directory: str = os.path.dirname(__file__)
    user_token_from_tg_bot: str = "7333919181:AAGjgPaKVUDbRyM9OCLIauoJeyO5XDHf2aE"

settings = Settings()
