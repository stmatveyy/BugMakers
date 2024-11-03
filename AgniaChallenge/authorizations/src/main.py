from fastapi import FastAPI
from fastapi import HTTPException

from .authorization_services import todoist
from .hackathon_utils import (
    save_authorization_data_and_return_response,
)
from authorizations.src.settings import base_hackathon_settings, todoist_auth_settings

app = FastAPI()

assert (
    base_hackathon_settings.user_token_from_tg_bot != ""
), "Укажите Telegram токен в settings.py"
assert (
    todoist_auth_settings.todoist_client_id != ""
), "Укажите Todoist Client ID в settings.py"
assert (
    todoist_auth_settings.todoist_client_secret != ""
), "Укажите Todoist Client Secret в settings.py"


@app.get("/todoist/authorize")
def authorize_in_todoist():
    return {"url": todoist.authorize()}


@app.get("/todoist/get-token", include_in_schema=False)
def get_todoist_token(
    code: str = None,
    state: str = None,
    error: str = None,
):
    if error == "invalid_application_status":
        raise HTTPException(status_code=500, detail="Invalid application status")
    elif error == "invalid_scope":
        raise HTTPException(status_code=400, detail="Invalid scope")
    elif error == "access_denied":
        raise HTTPException(status_code=403, detail="User denied authorization")

    authorization_token = todoist.callback(code, state, error)
    return save_authorization_data_and_return_response(
        authorization_token, system_name="Todoist"
    )


@app.post("/Kaiten/push-token")
def push_kaiten_token(authorization_token: str, error: str = None):
    if error == "invalid_application_status":
        raise HTTPException(status_code=500, detail="Invalid application status")
    elif error == "invalid_scope":
        raise HTTPException(status_code=400, detail="Invalid scope")
    elif error == "access_denied":
        raise HTTPException(status_code=403, detail="User denied authorization")

    return save_authorization_data_and_return_response(
        authorization_token, system_name="Kaiten"
    )


@app.post("/LLAMA/push-token")
def push_LLAMA_token(authorization_token: str, error: str = None):
    if error == "invalid_application_status":
        raise HTTPException(status_code=500, detail="Invalid application status")
    elif error == "invalid_scope":
        raise HTTPException(status_code=400, detail="Invalid scope")
    elif error == "access_denied":
        raise HTTPException(status_code=403, detail="User denied authorization")

    return save_authorization_data_and_return_response(
        authorization_token, system_name="LLAMA"
    )

@app.post("/Clockify/push-token")
def push_LLAMA_token(authorization_token: str, error: str = None):
    if error == "invalid_application_status":
        raise HTTPException(status_code=500, detail="Invalid application status")
    elif error == "invalid_scope":
        raise HTTPException(status_code=400, detail="Invalid scope")
    elif error == "access_denied":
        raise HTTPException(status_code=403, detail="User denied authorization")

    return save_authorization_data_and_return_response(
        authorization_token, system_name="Clockify"
    )
