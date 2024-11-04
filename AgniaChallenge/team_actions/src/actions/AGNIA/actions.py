import requests as rq

from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, HttpUrl
from requests.auth import HTTPBasicAuth
from team_actions.src.registration import register_action

authorization_data = {}


class LLMRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = 20
    temperature: Optional[float] = 0.73
    length_penalty: Optional[int] = -45


class LLMResponse(BaseModel):
    output: str


@register_action(
    system_type="AI",
    include_in_plan=True,
    signature="(prompt: str) -> LLMResponse",
    arguments=["prompt"],
    description="Generates response based on given prompt",
)
def ask_agnia(prompt: str) -> LLMResponse:
    res = rq.post(
        url="https://aes-agniachallenge-case.olymp.innopolis.university/llm/get-response",
        json={
            "team_id": authorization_data["AGNIA"],
            "temperature": 0.11,
            "max_tokens": 2000,
            "min_tokens": 300,
            "prompt": "Ты - бот-асстистент. Ответь на запрос на Русском языке" + prompt,
        },
    )

    res.raise_for_status()
    data = res.json()
    return data["output"]
