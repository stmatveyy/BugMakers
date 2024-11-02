from pydantic_settings import BaseSettings


class BaseHackathonSettings(BaseSettings):
    user_token_from_tg_bot: str = ""
    save_auth_data_endpoint: str = "https://aes-agniachallenge-case.olymp.innopolis.university/save-authorization-data"


class TodoistAuthSettings(BaseSettings):
    todoist_oauth_api_url: str = "https://todoist.com/oauth/authorize/"
    todoist_token_exchange_api_url: str = "https://todoist.com/oauth/access_token/"
    todoist_redirect_url: str = "http://localhost:9000"
    todoist_client_id: str = ""
    todoist_scope: str = "task:add,data:read,data:read_write,data:delete"
    todoist_state: str = "some_secret_state"
    todoist_client_secret: str = ""


base_hackathon_settings = BaseHackathonSettings()
todoist_auth_settings = TodoistAuthSettings()
