# TypeHints Definition
Id = Annotated[int, Field(description="Any ID represented as a string.")]
SpaceTitle = Annotated[str | int, Field(descripton="A well-crafted space title.")]
BoardTitle = Annotated[str, Field(descripton="A well-crafted board title.")]

BoardDescription = Annotated[str, Field(descripton="A brief board description")]
SpaceDescription = Annotated[str, Field(descripton="A brief space description")]

Date = Annotated[str, Field(description="A date when an entity was created")]


# Models definition

class Space(BaseModel):
    id: Id
    title: SpaceTitle
    created: Date
    updated: Date
    external_id: Optional[str, None]
    description: SpaceDescription

class Board(BaseModel):
    id: Id
    title: BoardTitle
    created: Date
    updated: Date
    external_id: Optional[str, None]
    description: BoardDescription
    columns: list[BoardColumn]
    lanes: list[BoardLanes]

class BoardColumn(BaseModel):
    id : Id	
    title: str	
    sort_order: int
    col_count: int	
    type: Literal[1, 2, 3]
    board_id: int	 
    column_id: Id	
    external_id: Optional[str, None]
    rules: int


class BoardLanes(BaseModel):
    id : Id	
    title: str	
    sort_order: int
    board_id: int
    condition: Literal[1, 2, 3]
    external_id: Optional[str, None]

class Column(BaseModel):
    id: Id
    title: str
    updated: str
    type: Literal[1, 2, 3]
    board_id: Id
    column_id: None
    external_id: Optional[str, None]


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
    due_date: Optional[Date, None]
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