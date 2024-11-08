# TypeHints Definition
Page = Annotated[str, default="1"]
WorkspaceName = Annotated[str, description="A name for a workspace"]

# Models definition

class User(BaseModel):
    id: Annotated[str, Field(example="64a687e29ae1f428e7ebe303")]
    email: str


class Workspace(BaseModel):
    workspaceName: WorkspaceName,
    id: Optional[str]


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



# API Calls Documentation
## create_new_time_entry
Description: 

Creates a new time entry for the user to track time from the beginning of work

Parameters:
- workspaceName(WorkspaceName): Name of the workspace
- billable(bool): Whether the time entry is billable of not
- description(Annotated[str, Field(ge=1, le=3000)]): Represents time entry description.
- end(Annotated[
        str, Field(description="Represents an end date in yyyy-MM-ddThh:mm:ssZ format")
    ]): Represents an end date in yyyy-MM-ddThh:mm:ssZ format.
- projectId(str): Represents project identifier across the system.
- start(Annotated[
        str,
        Field(description="Represents a start date in yyyy-MM-ddThh:mm:ssZ format."),
    ]): Represents a start date in yyyy-MM-ddThh:mm:ssZ format.
- tagIds(List[str]): Represents a list of tag ids.
- type(Literal["REGULAR", "BREAK"]): Valid time entry type.
- customAttributes(Optional[List[CustomAttribute]]): Represents a list of create custom field request objects.
- customField(Optional[List[CustomField]]): Represents a list of value objects for user’s custom fields.


Returns:
- created time entry (Time)


## get_specific_time_entry

Description:
Get a specific time entry by its description


Parameters:

- workspaceId(str): Id of a workspace
- timeEntryDescription(str): Description of time entry
- hydrated(Optional[str]): Flag to set whether to include additional information of a time entry or not.

Returns:
A time entry object (Time)

## add_new_project

Description: 
Adds new project

Parameters:
- workspaceName(WorkspaceName): A name of a workspace
- name(Annotated[str, Field(ge=2, le=250)]): A name for the project
- billable(Optional[bool]): Whether the project is billable or not

Returns:
Project object

## get_time_entries_for_user

Description:
Get all time entries for certain user

Parameters:
- workspaceId(str): Id of the workspace
- userId(Annotated[str, Field(example='5a0ab5acb07987125438b60f')]): User id
- description(Optional[str])A description of the time entry to search for
- project(Optional[str]): A project id that matches project_id field of the Time entry

Returns:
A list of Time objects

## create_workspace

Description:
Creates a workspace

Parameters:
- name(Annotated[str, Field(ge=2, le=250)]): A name of the workspace
- organizationId(Optional[str]): An organisation id

Returns:
A Workspace object

## get_all_workspace

Description:
Gets all workspaces for user

Parameters:

Returns:
A Workspace object
