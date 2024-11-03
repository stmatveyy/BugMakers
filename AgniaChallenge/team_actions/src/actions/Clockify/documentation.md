# TypeHints Definition
Page = Annotated[str, default="1"]


# Models definition

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
    sort-column: Literal["ID", "USER_ID", "START", "UPDATED_AT"]
    sort-order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]

class Client(BaseModel):
    workspaceId: str
    name: str
    sort-column: str
    sort-order: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    archived: bool

class Project(BaseModel):
    workspaceId: str
    name: str
    strict-name-search: str
    archived: str
    billable: str
    clients: str
    contains-client: str
    client-status: Literal["ACTIVE", "ARCHIVED", "ALL"]
    users: str
    contains-user: str
    user-status: Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]
    is-template: str
    sort-column: Literal["ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"]
    sort-order: Literal["ASCENDING", "DESCENDING"]
    hydrated: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    access: Literal["PUBLIC", "PRIVATE"]
    expense-limit: Annotated[str, default="20"]
    expense-date: str
    Annotated[str, Field( example="2024-12-31")]


class Task(BaseModel):
    projectId: str
    workspaceId: str
    name: str
    strict-name-search: str
    is-active: str
    page: Page
    page_size: Annotated[int, Field(ge=1, le=5000, default=50, description="Page size must be between 1 and 5000.")]
    sort-column: Literal["ID", "NAME"]
    sort-order: Literal["ASCENDING", "DESCENDING"]

class Tag(BaseModel):
    workspaceId: str
    name: str
    strict-name-search: str
    excluded-ids: str
    sort-column: Literal["ID", "NAME"]
    sort-order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page-size: Annotated[int, Field(ge=1, le=200, default=50, description="Page size must be between 1 and 200.")]
    archived: str

class Group(BaseModel):
    workspaceId: str
    project-id: str
    name: str
    sort-column: Literal["ID", "NAME"]
    sort-order: Literal["ASCENDING", "DESCENDING"]
    page: Page
    page_size: Annotated[int, Field(ge=1, le=5000, default=50, description="Page size must be between 1 and 5000.")]


class CustomAttribute(BaseModel):
    name: str
    name_space: str
    value: str

class CustomField(BaaseModel):
    customFieldId: str
    sourceType: Literal["WORKSPACE", "PROJECT", "TIMEENTRY"]
    value: str

class Time(BaseModel):
    workspaceId: str
    billable: bool
    customAttributes: conlist(CustomAttributes, min_items=1, max_items=5)
    customField: conlist(CustomField, min_items=1, max_items=50)
    description: Annotated[str, Field(ge=1, le=3000)]
    end: Annotated[str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")]
    projectId: str
    start: Annotated[str, Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format.")]
    tagIds: List[str]
    taskId: str
    type: Literal["REGULAR", "BREAK"]