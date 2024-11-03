import requests
from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, conlist, Field

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
    roles: Literal["WORKSPACE_ADMIN", "OWNER", "TEAM_MANAGER", "PROJECT_MANAGER"]

class Webhooks(BaseModel):
    workspaceId: str
    addonId: str

class Approval(BaseModel):
    workspaceId: str
    status: Literal["PENDING", "APPROVED", "WITHDRAWN_SUBMISSION", "WITHDRAWN_APPROVAL", "REJECTED"]
    sort_column: Literal["ID", "USER_ID", "START", "UPDATED_AT"]
    sort_order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]

class Client(BaseModel):
    workspaceId: str
    name: str
    sort_column: str
    sort_order: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    archived: bool

class Project(BaseModel):
    workspaceId: str
    name: str
    strict_name_search: str
    archived: str
    billable: str
    clients: str
    contains_client: str
    client_status: Literal["ACTIVE", "ARCHIVED", "ALL"]
    users: str
    contains_user: str
    user_status: Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]
    is_template: str
    sort_column: Literal["ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"]
    sort_order: Literal["ASCENDING", "DESCENDING"]
    hydrated: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    access: Literal["PUBLIC", "PRIVATE"]
    expense_limit: Annotated[str, Field(default="20")]
    expense_date: str
    Annotated[str, Field( example="2024-12-31")]


class Task(BaseModel):
    projectId: str
    workspaceId: str
    name: str
    strict_name_search: str
    is_active: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=5000, default=50, description="Page size must be between 1 and 5000.")]
    sort_column: Literal["ID", "NAME"]
    sort_order: Literal["ASCENDING", "DESCENDING"]

class Tag(BaseModel):
    workspaceId: str
    name: str
    strict_name_search: str
    excluded_ids: str
    sort_column: Literal["ID", "NAME"]
    sort_order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    archived: str

class Group(BaseModel):
    workspaceId: str
    project_id: str
    name: str
    sort_column: Literal["ID", "NAME"]
    sort_order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page_size: Annotated[int, Field(ge=1, le=5000, default=50, description="Page size must be between 1 and 5000.")]


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
    end: Annotated[str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")]
    projectId: str
    start: Annotated[str, Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format.")]
    tagIds: List[str]
    taskId: str
    type: Literal["REGULAR", "BREAK"]