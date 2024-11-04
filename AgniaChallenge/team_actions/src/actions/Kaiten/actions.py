import requests as rq

from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, HttpUrl
from requests.auth import HTTPBasicAuth
from team_actions.src.registration import register_action

authorization_data = {}

Id = Annotated[int, Field(description="Any ID represented as a string.")]
SpaceTitle = Annotated[str | int, Field(descripton="A well-crafted space title.")]
BoardTitle = Annotated[str, Field(descripton="A well-crafted board title.")]
BoardDescription = Annotated[str, Field(descripton="A brief board description")]
SpaceDescription = Annotated[str, Field(descripton="A brief space description")]
Date = Annotated[str, Field(description="A date when an entity was created")]

URL = "https://matvey-22.kaiten.ru/api/latest"


def get_res(res):
    res.raise_for_status()
    data = res.json()
    return data


def SpaceNameToId(auth, spaceName):
    spaces = rq.get(
        URL + "/spaces", headers={"Authorization": f"Bearer {auth['Kaiten']}"}
    ).json()

    try:
        sp_id = [sp for sp in spaces if sp["title"] == spaceName][0]["id"]

    except IndexError:
        return ({"reason": "Space not found"}, None)

    return (None, sp_id)


class Space(BaseModel):

    title: SpaceTitle
    external_id: Optional[Id]


class BoardColumn(BaseModel):
    id: Id
    title: str
    sort_order: int
    col_count: int
    type: Literal[1, 2, 3]
    board_id: int
    column_id: None
    external_id: Optional[str]
    rules: int


class BoardLanes(BaseModel):
    id: Id
    title: str
    sort_order: int
    board_id: int
    condition: Literal[1, 2, 3]
    external_id: Optional[str]


class Column(BaseModel):
    id: Id
    title: str
    updated: str
    type: Literal[1, 2, 3]
    board_id: Id
    column_id: None
    external_id: Optional[str]


class User(BaseModel):
    id: Id
    full_name: str
    username: str
    updated: Date
    created: Date
    activated: bool
    company_id: int
    default_space_id: int
    role: Literal[1, 2, 3]
    external: bool


class UserRole(BaseModel):
    name: str
    company_id: int
    created: Date
    updated: Date
    updated: int
    uid: str


class Card(BaseModel):
    id: Id
    title: str
    description: str
    asap: bool
    created: Date
    updated: Date
    due_date: Optional[Date]
    sort_order: int
    state: Literal[1, 2, 3]
    condition: Literal[1, 2]
    expires_later: bool
    parents_count: int
    children_count: int
    children_done: int
    blocking_card: bool
    blocked: bool
    board_id: Id
    column_id: Id
    lane_id: Id
    public: bool
    cardRole: int


class Board(BaseModel):
    id: Id
    title: BoardTitle
    created: Date
    updated: Date

    description: BoardDescription
    columns: list[BoardColumn]
    lanes: list[BoardLanes]


class Lane(BaseModel):
    title: str


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(title: SpaceTitle) -> Space",
    arguments=["title"],
    description="Creates new Space object",
)
def create_space(title: SpaceTitle) -> Space:

    res = rq.post(
        URL + "/spaces",
        headers={"Authorization": f"Bearer {authorization_data['Kaiten']}"},
        json={"title": title},
    )

    return get_res(res)


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(spaceName: str, title: str | int, columns: list[Column], \
                lanes: list[Lane], description: Optional[str]) -> Board",
    arguments=["title", "columns", "lanes", "description", "spaceName"],
    description="Create new Board object",
)
def create_board(
    spaceName: str,
    title: Optional[str | int],
    columns: List[Column],
    lanes: List[Lane],
    description: Optional[Optional[str]],
) -> Board:

    err, space_id = SpaceNameToId(auth=authorization_data, spaceName=spaceName)

    if err is not None:
        return err

    res = rq.post(
        URL + f"/spaces/{space_id}/boards",
        headers={"Authorization": f"Bearer {authorization_data['Kaiten']}"},
        json={
            "title": title,
            "columns": columns,
            "lanes": lanes,
            "top": 0,
            "left": 1168,
            "description": description,
        },
    )

    res.raise_for_status()
    data = res.json()
    return data


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(spaceName: str) -> Board",
    description="Get list of Boards",
    arguments=["spaceName"],
)
def get_boards_list(spaceName: str) -> List[Board]:
    err, space_id = SpaceNameToId(auth=authorization_data, spaceName=spaceName)

    if err:
        return err

    res = rq.get(
        URL + f"/spaces/{space_id}/boards",
        headers={"Authorization": f"Bearer {authorization_data['Kaiten']}"},
    )

    return get_res(res)


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    arguments=["board_id", "title", "sort_order", "type"],
    signature="(board_id: int, title: str, \
                sort_order: Optional[int], type: Literal[0, 1, 3]) -> BoardColumn",
    description="Create Column object",
)
def create_column(
    board_id: int, title: str, sort_order: Optional[int], type: Literal[0, 1, 3]
) -> BoardColumn:

    res = rq.post(
        URL + f"/boards/{board_id}/columns",
        headers={"Authorization": f"Bearer {authorization_data['Kaiten']}"},
        json={"title": title, "sort_order": sort_order, "type": type},
    )

    return get_res(res)


@register_action(
    system_type="task_tracker",
    include_in_plan=True,
    signature="(title: int | str, board_id: int, \
                asap: Optional[bool], due_date: Optional[Date], \
                sort_order: Optional[str], description: Optional[int | str]) -> Card",
    arguments=["title", "board_id", "asap", "due_date", "soet_order", "description"],
    description="create Card object",
)
def create_card(
    title: int | str,
    board_id: int,
    asap: Optional[bool],
    due_date: Optional[Date],
    sort_order: Optional[str],
    description: Optional[int | str],
) -> Card:

    res = rq.post(
        URL,
        headers={"Authorization": f"Bearer {authorization_data['Kaiten']}"},
        json={
            "title": title,
            "board_id": board_id,
            "asap": asap,
            "sort_order": sort_order,
            "description": description,
        },
    )

    return get_res(res)
