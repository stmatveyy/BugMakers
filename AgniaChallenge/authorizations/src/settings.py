from pydantic_settings import BaseSettings


class BaseHackathonSettings(BaseSettings):
    user_token_from_tg_bot: str = "7333919181:AAGjgPaKVUDbRyM9OCLIauoJeyO5XDHf2aE"
    save_auth_data_endpoint: str = "https://aes-agniachallenge-case.olymp.innopolis.university/save-authorization-data"


class TodoistAuthSettings(BaseSettings):
    todoist_oauth_api_url: str = "https://todoist.com/oauth/authorize/"
    todoist_token_exchange_api_url: str = "https://todoist.com/oauth/access_token/"
    todoist_redirect_url: str = "http://localhost:9000"
    todoist_client_id: str = "51379933"
    todoist_scope: str = "task:add,data:read,data:read_write,data:delete"
    todoist_state: str = "some_secret_state"
    todoist_client_secret: str = "6409a46c4d38fc1d4f3b853be11a9fc580beca39"

class GitFlameAuthSettings(BaseSettings):
    ...

base_hackathon_settings = BaseHackathonSettings()
todoist_auth_settings = TodoistAuthSettings()
