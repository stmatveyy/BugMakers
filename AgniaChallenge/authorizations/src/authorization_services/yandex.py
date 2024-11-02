import requests
from fastapi import HTTPException

from authorizations.src.settings import todoist_auth_settings, yandex_auth_settings


def authorize():
    authorization_url = (
        f"{yandex_auth_settings.yandex_oauth_api_url}?"
        f"client_id={yandex_auth_settings.yandex_client_id}"
    )

    return authorization_url


def callback(code: str = None, error: str = None):

    token_params = {
        "client_id": yandex_auth_settings.yandex_client_id,
        "client_secret": yandex_auth_settings.yandex_client_secret,
        "redirect_uri": yandex_auth_settings.yandex_redirect_uri,
    }

    try:
        response = requests.post(
            yandex_auth_settings.yandex_oauth_api_url, data=token_params
        )

        response.raise_for_status()
        response_data = response.json()

        return response_data["access_token"]

    except requests.HTTPError:
        error_data = response.json()
        # This could happen if the code is used more than once, or if it has expired.
        if error_data.get("error") == "bad_authorization_code":
            raise HTTPException(status_code=400, detail="Bad authorization code")
        # client_id or client_secret parameters are incorrect:
        elif error_data.get("error") == "incorrect_application_credentials":
            raise HTTPException(
                status_code=401, detail="Incorrect application credentials"
            )
        else:
            raise HTTPException(status_code=500, detail="Token exchange failed")
    except requests.RequestException as req_err:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to communicate with Todoist: {str(req_err)}",
        )
