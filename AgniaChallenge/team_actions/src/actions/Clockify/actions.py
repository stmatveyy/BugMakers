import requests
from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field

from team_actions.src.registration import register_action


authorization_data = {}
# Держите это поле пустым изначально.
# После регистрации действий в системе, сюда будут автоматически
# добавлены авторизационные данные участников.

# Определяем Type Hints для входных параметров
Page = Annotated[str, Field(default="1")]

# Определяем модели данных для выходных параметров


class User(BaseModel):
    file: str


class Workspace(BaseModel):
    roles: Optional[
        Literal["WORKSPACE_ADMIN", "OWNER", "TEAM_MANAGER", "PROJECT_MANAGER"]
    ]


class Webhooks(BaseModel):
    workspaceId: str
    addonId: str


class Approval(BaseModel):
    workspaceId: str
    status: Optional[
        Literal[
            "PENDING",
            "APPROVED",
            "WITHDRAWN_SUBMISSION",
            "WITHDRAWN_APPROVAL",
            "REJECTED",
        ]
    ]
    sort_column: Optional[Literal["ID", "USER_ID", "START", "UPDATED_AT"]]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=200,
                default=50,
                description="Page size must be between 1 and 200.",
            ),
        ]
    ]


class Client(BaseModel):
    workspaceId: str
    name: Optional[str]
    sort_column: Optional[str]
    sort_order: Optional[str]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=200,
                default=50,
                description="Page size must be between 1 and 200.",
            ),
        ]
    ]
    archived: Optional[bool]


class Project(BaseModel):
    workspaceId: str
    name: Optional[str]
    strict_name_search: Optional[str]
    archived: Optional[str]
    billable: Optional[str]
    clients: Optional[str]
    contains_client: Optional[str]
    client_status: Optional[Literal["ACTIVE", "ARCHIVED", "ALL"]]
    users: Optional[str]
    contains_user: Optional[str]
    user_status: Optional[Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]]
    is_template: Optional[str]
    sort_column: Optional[
        Literal["ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"]
    ]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]
    hydrated: Optional[str]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=200,
                default=50,
                description="Page size must be between 1 and 200.",
            ),
        ]
    ]
    access: Optional[Literal["PUBLIC", "PRIVATE"]]
    expense_limit: Optional[Annotated[str, Field(default="20")]]
    expense_date: Optional[Annotated[str, Field(example="2024-12-31")]]


class Task(BaseModel):
    projectId: str
    workspaceId: str
    name: Optional[str]
    strict_name_search: Optional[str]
    is_active: Optional[str]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=5000,
                default=50,
                description="Page size must be between 1 and 5000.",
            ),
        ]
    ]
    sort_column: Optional[Literal["ID", "NAME"]]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]


class Tag(BaseModel):
    workspaceId: str
    name: Optional[str]
    strict_name_search: Optional[str]
    excluded_ids: Optional[str]
    sort_column: Optional[Literal["ID", "NAME"]]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=200,
                default=50,
                description="Page size must be between 1 and 200.",
            ),
        ]
    ]
    archived: Optional[str]


class Group(BaseModel):
    workspaceId: str
    project_id: Optional[str]
    name: Optional[str]
    sort_column: Optional[Literal["ID", "NAME"]]
    sort_order: Optional[Literal["ASCENDING", "DESCENDING"]]
    page: Optional[Page]
    page_size: Optional[
        Annotated[
            int,
            Field(
                ge=1,
                le=5000,
                default=50,
                description="Page size must be between 1 and 5000.",
            ),
        ]
    ]


class CustomAttribute(BaseModel):
    name: str
    name_space: str
    value: str


class CustomField(BaseModel):
    customFieldId: str
    sourceType: Literal["WORKSPACE", "PROJECT", "TIMEENTRY"]
    value: str


class Time(BaseModel):
    workspaceId: str
    billable: bool
    customAttributes: Optional[List[CustomAttribute]]
    customField: Optional[List[CustomField]]
    description: Annotated[str, Field(ge=1, le=3000)]
    end: Annotated[
        str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")
    ]
    projectId: str
    start: Annotated[
        str,
        Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format."),
    ]
    tagIds: List[str]
    taskId: str
    type: Literal["REGULAR", "BREAK"]


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(workspaceId: str, billable: bool, customAttributes: Optional[List[CustomAttribute]] = None, customField: Optional[List[CustomField]] = None, description: Annotated[str, Field(ge=1, le=3000)], end: Annotated[str, Field(description=\"Represents an end date in yyyy-MM-ddThh:mm:ssZ format\")], projectId: str, start:Annotated[str, Field(description=\"Represents a start date in yyyy-MM-ddThh:mm:ssZ format.\")], tagIds: List[str], taskId: str, type: Literal['REGULAR', 'BREAK']) -> Time",
    arguments=[
        "workspaceId",
        "billable",
        "customAttributes",
        "customField",
        "description",
        "end",
        "projectId",
        "start",
        "tagIds",
        "taskId",
        "type",
    ],
    description="Creates a new time",
)
def create_new_time_entry(
    workspaceId: str,
    billable: bool,
    description: Annotated[str, Field(ge=1, le=3000)],
    end: Annotated[
        str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")
    ],
    projectId: str,
    start: Annotated[
        str,
        Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format."),
    ],
    tagIds: List[str],
    taskId: str,
    type: Literal["REGULAR", "BREAK"],
    customAttributes: Optional[List[CustomAttribute]] = None,
    customField: Optional[List[CustomField]] = None,
) -> Time:
    # Логика вызова API Clockify для создания времени входа начало работы над проектом
    response = requests.post(
        "",
        headers={"Authorization": f"Bearer {authorization_data['Clockify']}"},
        json={
            "workspaceId": workspaceId,
            "billable": billable,
            "description": description,
            "end": end,
            "projectId": projectId,
            "start": start,
            "tagIds": tagIds,
            "taskId": taskId,
            "type": type,
            "customAttributes": customAttributes,
            "customField": customField,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data
