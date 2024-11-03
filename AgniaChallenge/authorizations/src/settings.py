from pydantic_settings import BaseSettings


class BaseHackathonSettings(BaseSettings):
    user_token_from_tg_bot: str = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjExNDJlNjMtMjFjNS00MTY3LWEzMWQtM2M1Yjk2NzIzNTlhIiwiZXhwIjoxNzMwNjY5NjYxLjk3NzY4OCwiaXNzIjoiYmFja2VuZDphY2Nlc3MtdG9rZW4ifQ.ygi6RJmf92QdKtZxnCw_6ChCo6M1wCF9w5R9EgTQWX0"
    )
    save_auth_data_endpoint: str = (
        "https://aes-agniachallenge-case.olymp.innopolis.university/save-authorization-data"
    )


class TodoistAuthSettings(BaseSettings):
    todoist_oauth_api_url: str = "https://todoist.com/oauth/authorize/"
    todoist_token_exchange_api_url: str = "https://todoist.com/oauth/access_token/"
    todoist_redirect_url: str = "http://localhost:9000"
    todoist_client_id: str = "15d3a6c1c1a34ad591d7233b05d59a6d"
    todoist_scope: str = "task:add,data:read,data:read_write,data:delete"
    todoist_state: str = "some_secret_state"
    todoist_client_secret: str = "96e9b8009985409dae8b3cdad4ea0e9c"


class YandexAuthSettings(BaseSettings):
    yandex_oauth_api_url: str = "https://oauth.yandex.ru/authorize"
    yandex_client_id: str = "97342af268a64520889612d95ad90e4b"
    yandex_client_secret: str = "7693f1594df84217adb2a62ecc785e30"
    yandex_redirect_uri: str = "https://mlbuy.ru:443"


base_hackathon_settings = BaseHackathonSettings()
todoist_auth_settings = TodoistAuthSettings()
yandex_auth_settings = YandexAuthSettings()
