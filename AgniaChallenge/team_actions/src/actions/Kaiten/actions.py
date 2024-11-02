import os
import requests as rq
import json as js

from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, HttpUrl
from requests.auth import HTTPBasicAuth
from team_actions.src.registration import register_action



Id = Annotated[int, Field(description="Any ID represented as a string.")] 
SpaceTitle = Annotated[str, Field(descripton="A well-crafted space title.")]
BoardTitle = Annotated[str, Field(descripton="A well-crafted board title.")]
BoardDescription = Annotated[str, Field(descripton="A brief board description")] 
SpaceDescription = Annotated[str, Field(descripton="A brief space description")]




class Space(BaseModel):

    title: SpaceTitle
    external_id: Optional[Id]

@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(title: SpaceTitle, externel_id: Optional[Id] = None)",
    arguments=[
        "title",
        "externel_id"
    ],
    description="Creates new Space object")
def create_task(title: SpaceTitle, externel_id: Optional[Id] = None) -> Space:

    response = rq.post(
        "https://example.kaiten.ru/api/latest/spaces",
        headers={
            "Authorization": f"Bearer a93ac0b1-c4be-42e5-a59e-ff514b0e279b"
        },
        json = {
            "title": title,
            "externel_id": externel_id
        }
    )

    response.raise_for_status()
    data = response.json()
    return data

