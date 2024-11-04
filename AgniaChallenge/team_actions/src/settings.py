import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    team_id: str = "b051d03a-817d-4489-b198-f6b154a4c65f"
    backend_api: str = "https://aes-agniachallenge-case.olymp.innopolis.university/"
    root_directory: str = os.path.dirname(__file__)
    user_token_from_tg_bot: str = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjExNDJlNjMtMjFjNS00MTY3LWEzMWQtM2M1Yjk2NzIzNTlhIiwiZXhwIjoxNzMwNzU2ODgyLjkxMTUyNSwiaXNzIjoiYmFja2VuZDphY2Nlc3MtdG9rZW4ifQ.xUXfoVybC-vxnDLkUO69ldwRDUyH0A5eX8gdGPoCKQ0"
    )


settings = Settings()
