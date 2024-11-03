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
    id: Annotated[str, Field(example="64a687e29ae1f428e7ebe303")]
    email: str


class Workspace(BaseModel):
    id: str
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
    signature="(workspaceName: str, workspaceId: str, billable: Optional[bool],description: Optional[Annotated[str, Field(ge=1, le=3000)]],end: Optional[Annotated[str, Field(description=\"Represents an end date in yyyy-MM-ddThh:mm:ssZ format\")]],projectId: Optional[str],start: Optional[Annotated[str,Field(description=\"Represents a start date in yyyy-MM-ddThh:mm:ssZ format.\"),]],tagIds: Optional[List[str]],taskId: Optional[str],type: Optional[Literal[\"REGULAR\", \"BREAK\"]],customAttributes: Optional[List[CustomAttribute]] = None,customField: Optional[List[CustomField]] = None,) -> Time",
    arguments=[
        "workspaceName",
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
    workspaceName: str,
    workspaceId: str,
    billable: Optional[bool],
    description: Optional[Annotated[str, Field(ge=1, le=3000)]],
    end: Optional[Annotated[
        str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")
    ]],
    projectId: Optional[str],
    start: Optional[Annotated[
        str,
        Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format."),
    ]],
    tagIds: Optional[List[str]],
    taskId: Optional[str],
    type: Optional[Literal["REGULAR", "BREAK"]],
    customAttributes: Optional[List[CustomAttribute]] = None,
    customField: Optional[List[CustomField]] = None
) -> Time:
    # Логика вызова API Clockify для создания времени входа начало работы над проектом

    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "roles": Optional[Literal["WORKSPACE_ADMIN", "OWNER", "TEAM_MANAGER", "PROJECT_MANAGER"]],
        },
    )

    needed_workspace = [sp for sp in response.json() if sp["name"] == workspaceName][0]

    needed_ws_id = needed_workspace["id"]

    response.raise_for_status()
    data = response.json()

    response = requests.post(
        f"https://api.clockify.me/api/v1/workspaces/{needed_ws_id}/time-entries",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
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


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(workspaceId: str, page: Optional[Annotated[int, Field(ge=1)]], page_size: Optional[Annotated[int, Field(ge=1, le=1000, default=10)]]) -> List[Time]",
    arguments=["workspaceId", "page", "page_size"],
    description="Creates a new time",
)
def get_all_progress_time(
    workspaceId: str,
    page: Optional[Annotated[int, Field(ge=1)]],
    page_size: Optional[Annotated[int, Field(ge=1, le=1000, default=10)]],
) -> List[Time]:
    # Получение всех временных отрезков
    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries/status/in-progress",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "workspaceId": workspaceId,
            "page": page,
            "page_size": page_size,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(workspaceId: str, id: Annotated[str, Field(example='64c777ddd3fcab07cfbb210c')], hydrated: Optional[str] = None) -> Time",
    arguments=["workspaceId", "id", "hydrated"],
    description="Creates a new time",
)
def get_specific_time_entry(
    workspaceId: str,
    id: Annotated[str, Field(example="64c777ddd3fcab07cfbb210c")],
    hydrated: Optional[str] = None,
) -> Time:
    # Получение итогового времени работы над проектом ver.2
    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/time-entries/{id}",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "workspaceId": workspaceId,
            "id": id,
            "hydrated": hydrated,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(workspaceId: str, billable: Optional[bool] = None, clientId: Optional[str] = None, color: Optional[Annotated[str, Field(pattern=r'^#(?:[0-9a-fA-F]{6}){1}$')]] = None, costRate: Optional[List] = None, estimate: Optional[List] = None, hourlyRate: Optional[List] = None, isPublic: Optional[bool] = None, memberships: Optional[List] = None, name: Annotatad[str, Field(ge=2, le=250)], note: Optional[Annotated[str, Field(le=1684)]], tasks: Optional[List] = None) -> Project",
    arguments=["workspaceId", "billable", "clientId", "note", "name", "color", "costRate", "estimate", "hourlyRate", "isPublic", "memberships", "tasks"],
    description="Creates a new time",
)
def add_new_project(
    workspaceId: str,
    name: Annotated[str, Field(ge=2, le=250)],
    note: Optional[Annotated[str, Field(le=1684)]] = None,
    billable: Optional[bool] = None,
    clientId: Optional[str] = None,
    color: Optional[Annotated[str, Field(pattern="^#(?:[0-9a-fA-F]{6}){1}$")]] = None,
    costRate: Optional[List] = None,
    estimate: Optional[List] = None,
    hourlyRate: Optional[List] = None,
    isPublic: Optional[bool] = None,
    memberships: Optional[List] = None,
    tasks: Optional[List] = None,
) -> Project:
    response = requests.post(
        f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/projects",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "workspaceId": workspaceId,
            "name": name,
            "note": note,
            "billable": billable,
            "clientId": clientId,
            "color": color,
            "costRate": costRate,
            "estimate": estimate,
            "hourlyRate": hourlyRate,
            "isPublic": isPublic,
            "memberships": memberships,
            "tasks": tasks,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  
    signature="(workspaceId: str, userId: Annotated[str, Field(example='5a0ab5acb07987125438b60f')], description: Optional[str] = None, start: Optional[Annotated[str, Field(example='start=2020-01-01T00:00:00Z')]] = None, end: Optional[Annotated[str, Field(example='end=2021-01-01T00:00:00Z')]] = None, project: Optional[str] = None, task: Optional[str] = None, tags: Optional[str] = None, project_required: Optional[str] = None, task_required: Optional[str] = None, hydrated: Optional[str] = None, page: Optional[Annotated[str, Field(default='1')]] = None, page_size: Optional[Annotated[str, Field(default='50')]] = None, in_progress: Optional[bool] = None, get_week_before = Optional[str] = None) -> List[Time]",
    arguments=["workspaceId", "userId", "description", "start", "end", "project", "task", "tags", "project_required", "task_required",  "hydrated", "page", "page_size", "in_progress", "get_week_before"],
    description="Creates a new time",
)
def get_time_entries_for_user(
    workspaceId: str, 
    userId: Annotated[str, Field(example='5a0ab5acb07987125438b60f')], 
    description: Optional[str] = None, 
    start: Optional[Annotated[str, Field(example='start=2020-01-01T00:00:00Z')]] = None, 
    end: Optional[Annotated[str, Field(example='end=2021-01-01T00:00:00Z')]] = None, 
    project: Optional[str] = None, 
    task: Optional[str] = None, 
    tags: Optional[str] = None, 
    project_required: Optional[str] = None, 
    task_required: Optional[str] = None, 
    hydrated: Optional[str] = None, 
    page: Optional[Annotated[str, Field(default='1')]] = None, 
    page_size: Optional[Annotated[str, Field(default='50')]] = None, 
    in_progress: Optional[bool] = None, 
    get_week_before: Optional[str] = None
    ) -> List[Time]:
    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces/{workspaceId}/user/{userId}/time-entries",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "workspaceId": workspaceId,
            "description": description,
            "start": start,
            "end": end,
            "project": project,
            "task": task,
            "tags": tags,
            "project_required": project_required,
            "task_required": task_required,
            "hydrated": hydrated,
            "page": page,
            "page_size": page_size,
            "in_progress": in_progress,
            "get_week_before": get_week_before,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(cakeOrganizationId: Optional[str] = None, name: Annotated[str, Field(ge=2, le=250)], organizationId: Optional[str] = None) -> Workspace",
    arguments=["cakeOrganizationId", "name", "organizationId"],
    description="Creates a new time",
)
def create_workspace(
    name: Annotated[str, Field(ge=2, le=250)],
    cakeOrganizationId: Optional[str] = None,
    organizationId: Optional[str] = None,
) -> Workspace:
    response = requests.post(
        f"https://api.clockify.me/api/v1/workspaces",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "name": name,
            "cakeOrganizationId": cakeOrganizationId,
            "organizationId": organizationId,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data

@register_action(
    system_type="time_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(roles: Optional[str]) -> Workspace",
    arguments=["roles"],
    description="Creates a new time",
)
def get_all_workspace(
    roles: Optional[str]
) -> Workspace:
    response = requests.get(
        f"https://api.clockify.me/api/v1/workspaces",
        headers={"X-Api-Key": f"{authorization_data['Clockify']}"},
        json={
            "roles": roles,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data