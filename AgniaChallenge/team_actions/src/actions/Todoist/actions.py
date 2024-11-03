import requests
from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, HttpUrl

from team_actions.src.registration import register_action


authorization_data = {}
# Держите это поле пустым изначально.
# После регистрации действий в системе, сюда будут автоматически
# добавлены авторизационные данные участников.


# Определяем Type Hints для входных параметров
Id = Annotated[str, Field(pattern="^[0-9]+$")]
TaskName = Annotated[str, Field(description="Task name")]
Datetime = Annotated[
    str, Field(pattern=r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")
]
ShortDatetime = Annotated[str, Field(pattern=r"^\d{4}-\d{2}-\d{2}$")]
DueString = Annotated[str, Field(description="Due date in English", example="tomorrow")]
DueLang = Annotated[str, Field(pattern="^[a-z]{2}$", default="en")]
DurationUnit = Literal["minute", "day"]
Priority = Annotated[int, Field(ge=1, le=4)]
ProjectId = str


# Определяем модели данных для выходных параметров
class Due(BaseModel):
    string: Optional[DueString]
    date: Optional[ShortDatetime]
    is_recurring: bool
    datetime: Optional[Datetime]
    timezone: Optional[str]


class Duration(BaseModel):
    amount: Optional[int]
    unit: Optional[DurationUnit]


class Task(BaseModel):
    id: Id
    assigner_id: Optional[Id]
    assignee_id: Optional[Id]
    project_id: Id
    section_id: Optional[Id]
    parent_id: Optional[Id]
    order: int
    content: TaskName
    description: Optional[str]
    is_completed: bool
    labels: Optional[List[str]]
    priority: Priority
    comment_count: int
    creator_id: Id
    created_at: Datetime
    due: Optional[Due]
    url: HttpUrl
    duration: Optional[Duration]


class Project(BaseModel):
    name: str
    parent_id: Optional[str]
    color: Optional[str]
    is_favorite: Optional[bool]
    view_style: Optional[str]


class Sections(BaseModel):
    # id: Id
    project_id: ProjectId
    order: Annotated[int, Field(ge=1)]
    name: str


@register_action(
    system_type="task_tracker",
    include_in_plan=True,  # Действие может быть использовано в плане
    signature="(content: TaskName, description: Optional[str] = None, project_id: Optional[ProjectId] = None, section_id: Optional[SectionId] = None, labels: Optional[List[str]] = None, priority: Optional[Priority] = None, due_string: Optional[DueString] = None, due_date: Optional[ShortDatetime] = None, due_datetime: Optional[Datetime] = None, due_lang: Optional[DueLang] = None, duration: Optional[Duration] = None, duration_unit: Optional[DurationUnit] = None) -> Task",
    arguments=[
        "content",
        "description",
        "project_id",
        "section_id",
        "labels",
        "priority",
        "due_string",
        "due_date",
        "due_datetime",
        "due_lang",
        "duration",
        "duration_unit",
    ],
    description="Creates a new task",
)
def create_task(
    content: TaskName,
    description: Optional[str] = None,
    project_id: Optional[Id] = None,
    section_id: Optional[Id] = None,
    labels: Optional[List[str]] = None,
    priority: Optional[Priority] = 1,
    due_string: Optional[DueString] = None,
    due_lang: Optional[DueLang] = "en",
    due_date: Optional[ShortDatetime] = None,
    due_datetime: Optional[Datetime] = None,
    duration: Optional[Duration] = None,
    duration_unit: Optional[DurationUnit] = None,
) -> Task:
    # Логика вызова API Todoist для создания задачи
    response = requests.post(
        "https://api.todoist.com/rest/v2/tasks",
        headers={"Authorization": f"Bearer {authorization_data['Todoist']}"},
        json={
            "content": content,
            "description": description,
            "project_id": project_id,
            "section_id": section_id,
            "labels": labels,
            "priority": priority,
            "due_string": due_string,
            "due_lang": due_lang,
            "due_date": due_date,
            "due_datetime": due_datetime,
            "duration": duration,
            "duration_unit": duration_unit,
        },
    )

    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(name: str, parent_id: Optional[str] = None, color: Optional[str] = None, is_favorite: Optional[bool] = None, view_style: Optional[str] = None) -> Project",
    arguments=[
        "name",
        "parent_id",
        "color",
        "is_favorite",
        "view_style",
    ],
    description="Creates a new project",
)
def create_new_project(
    name: str,
    parent_id: Optional[str] = None,
    color: Optional[str] = None,
    is_favorite: Optional[bool] = None,
    view_style: Optional[str] = None,
) -> Project:
    # Логика вызова API Todoist для создания задачи
    response = requests.post(
        "https://api.todoist.com/rest/v2/projects",
        headers={"Authorization": f"Bearer {authorization_data['Todoist']}"},
        json={
            "name": name,
            "parent_id": parent_id,
            "color": color,
            "is_favorite": is_favorite,
            "view_style": view_style,
        },
    )
    response.raise_for_status()
    data = response.json()
    return data


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(project_id: str, order: Annotated[int, Field(ge=1)] = None, name: str = None) -> Sections",
    arguments=[
        # "id",
        "project_id",
        "order",
        "name",
    ],
    description="Creates a new section",
)
def create_new_section(
    # id: Id,
    project_id: str,
    name: str,
    order: Annotated[int, Field(ge=1)] = None,
) -> Sections:
    response = requests.post(
        "https://api.todoist.com/rest/v2/sections",
        headers={"Authorization": f"Bearer {authorization_data['Todoist']}"},
        json={
            "id": id,
            "project_id": project_id,
            "order": order,
            "name": name,
        },
    )
    response.raise_for_status()
    data = response.json()
    return data
