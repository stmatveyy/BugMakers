import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    team_id: str = "b051d03a-817d-4489-b198-f6b154a4c65f"
    backend_api: str = "https://aes-agniachallenge-case.olymp.innopolis.university/"
    root_directory: str = os.path.dirname(__file__)
    user_token_from_tg_bot: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmYzNzY4NmYtYmZiNy00YWZiLTgyZDQtMGNiMDAwMzJjMjhhIiwiZXhwIjoxNzMwNTc2NjE2LjU4ODQyNywiaXNzIjoiYmFja2VuZDphY2Nlc3MtdG9rZW4ifQ.gTynVUCajiY6ZPf7T9e5IbeDmi_iPVZr86MPJ8uDDCs"

settings = Settings()
