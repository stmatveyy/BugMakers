from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from authorizations.src.authorization_services import todoist, yandex
from authorizations.src.hackathon_utils import (
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

@app.get("/yandex/authorize")
def authorize_in_yandex():
    return {"url": yandex.authorize()}


@app.get("/yandex/get-token")
def get_yandex_token(
    code: str = None,
    error: str = None
):
    if error == "invalid_application_status":
        raise HTTPException(status_code=500, detail="Invalid application status")
    elif error == "invalid_scope":
        raise HTTPException(status_code=400, detail="Invalid scope")
    elif error == "access_denied":
        raise HTTPException(status_code=403, detail="User denied authorization")

    authorization_token = yandex.callback(code=code, error=error)

    return save_authorization_data_and_return_response(
        authorization_token, system_name="Yandex"
    )

if __name__ == '__main__':
    uvicorn.run("proxy_server:app",
                host="0.0.0.0",
                port=9000,
                reload=True,
                ssl_keyfile="/etc/letsencrypt/live/mlbuy.ru/privkey.pem", 
                ssl_certfile="/etc/letsencrypt/live/mlbuy.ru/fullchain.pem"
                )





