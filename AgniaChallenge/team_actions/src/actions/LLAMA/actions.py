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
    system_type="ask_lama",
    include_in_plan=False,
    signature="(prompt: str, temperature: Optional[float] = 0, max_tokens: Optional[int] = 20, length_penalty: Optional[int] = -45) -> LLMResponse",
    arguments=["prompt", "max_tokens", "temperature", "length_penalty"],
    description="Generates response based on given prompt",
)
def ask_lama(
             prompt: str,
             temperature: Optional[float] = 0,
             max_tokens: Optional[int] = 20,
             length_penalty: Optional[int] = -45) -> LLMResponse:
    
    res = rq.post(url="https://aes-agniachallenge-case.olymp.innopolis.university/llm/get-response",
                  json={"team_id": authorization_data["LLAMA"], 
                        "prompt": "Ответь на следующий запрос на Русском языке: " + prompt, 
                        "temperature": temperature, 
                        "max_tokens": max_tokens,
                        "length_penalty": length_penalty})
    
    res.raise_for_status()
    data = res.json()
    return LLMResponse(output=data["output"])