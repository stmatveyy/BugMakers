# TypeHints Definition
Id = Annotated[str, Field(pattern="^[0-9]+$")]
UserId = Annotated[Id]
TaskId = Annotated[Id]
ProjectId = str
TaskName = Annotated[str, Field(description="A well-crafted task name.")]
Datetime = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")]
ShortDatetime = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}$")]
TimezoneString = Annotated[str, Field(description="Timezone definition in tzdata-compatible format or UTC offset (e.g. Europe/Berlin)")]
DueString = Annotated[str, Field(description="Due date must match english language", example="tomorrow")]
DueLang = Annotated[str, Field(pattern="^[a-z]{2}$", default="en")]
DurationUnit = Literal['minute', 'day']
Priority = Annotated[int, Field(ge=1, le=4)]
EmptyDict = Annotated[dict()]
TaskDifficulty = Annotated[Literal["easy", "medium", "hard"]]


# Models definition
class Due(BaseModel):
    string: Optional[DueString]
    date: Optional[ShortDatetime]
    is_recurring: bool
    datetime: Optional[Datetime]
    timezone: Optional[TimezoneString]


class Duration(BaseModel):
    amount: Optional[int]
    unit: Optional[DurationUnit]


class Task(BaseModel):
    id: TaskId
    assigner_id: Optional[UserId]
    assignee_id: Optional[UserId]
    project_id: Id
    section_id: Optional[Id]
    parent_id: Optional[TaskId]
    order: int
    content: TaskName
    description: Optional[str]
    is_completed: bool
    labels: Optional[List[str]]
    priority: Priority
    comment_count: int
    creator_id: UserId
    created_at: Datetime
    due: Optional[Due]
    url: HttpUrl
    duration: Optional[Duration]


class ActiveTasks(BaseModel):
    result: List[Task]

class Project(BaseModel):
    name: str
    parent_id: Optinal[str]
    color: Optinal[str]
    is_favorite:Optional[bool]
    view_style: Optional[str]

class Sections(BaseModel):
    id: Id
    project_id: ProjectId
    order: Optional[Annotated[int, Field(ge=1)]]
    name: str

class Entity(BaseModel):
    name: str
    id: Id


# API Calls Documentation
## create_task

Description:
Creates a new task in the system with optional parameters like descriptions, project and section IDs, and duration.

Parameters:
- content (TaskName): The name of the task.
- description (Optional[str]): A brief description of the task.
- project_id (Optional[Id]): The task project ID. If not set, task is put to user's Inbox.
- section_id (Optional[Id]): ID of section to put task into.
- labels (Optional[List[str]]): A list of names of objects or events that might be associated with the task.
- priority (Optional[Priority]): Task priority from 1 (normal) to 4 (urgent).
- due_string (Optional[DueString]): Human-defined task due date (e.g., 'next Monday', 'Tomorrow').
- due_lang (Optional[DueLang]): 2-letter language code.
- due_date (Optional[ShortDatetime]): Specific date in YYYY-MM-DD format relative to user’s timezone.
- due_datetime (Optional[Datetime]): Specific date and time in RFC3339 format, e.g. 2023-10-05T14:48:00-05:00.
- duration (Optional[Duration]): A dictionary representing a task duration.
- duration_unit (Optional[DurationUnit]): The unit of time that the duration field above represents.

Returns:
- created_task (Task)

## create_new_project

Description:
Creates a new project in the system with optional parameters like parent_id, parent_id and is_favourite, and color and view_style.

Parameters:
- name (str): The name of the project.
- parent_id (Optional[str]): An Id of the parent project
- color(Optional[str]): The color of the project icon in the hexidecimal format, e.g. #96c3eb
- is_favorite(Optional[bool]): Whether the project is a favorite (a true or false value)
- view_style(Optional[str]): A string value (either "list" or "board"). This determines the way the project is displayed within the Todoist clients. 

## create_new_section

Description: Creates a new section wthin a project

Parameters:
- name (str): The name of the section.
- project_id (str): Project ID this section should belong to
- order(Optional[Annotated[int, Field(ge=1)]]): Order among other sections in a project

