from pydantic_settings import BaseSettings


class BaseHackathonSettings(BaseSettings):
    user_token_from_tg_bot: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmYzNzY4NmYtYmZiNy00YWZiLTgyZDQtMGNiMDAwMzJjMjhhIiwiZXhwIjoxNzMwNTc2NjE2LjU4ODQyNywiaXNzIjoiYmFja2VuZDphY2Nlc3MtdG9rZW4ifQ.gTynVUCajiY6ZPf7T9e5IbeDmi_iPVZr86MPJ8uDDCs"
    save_auth_data_endpoint: str = "https://aes-agniachallenge-case.olymp.innopolis.university/save-authorization-data"


class TodoistAuthSettings(BaseSettings):
    todoist_oauth_api_url: str = "https://todoist.com/oauth/authorize/"
    todoist_token_exchange_api_url: str = "https://todoist.com/oauth/access_token/"
    todoist_redirect_url: str = "http://localhost:9000"
    todoist_client_id: str = "15d3a6c1c1a34ad591d7233b05d59a6d"
    todoist_scope: str = "task:add,data:read,data:read_write,data:delete"
    todoist_state: str = "some_secret_state"
    todoist_client_secret: str = "96e9b8009985409dae8b3cdad4ea0e9c"

class GitFlameAuthSettings(BaseSettings):
    ...

base_hackathon_settings = BaseHackathonSettings()
todoist_auth_settings = TodoistAuthSettings()
