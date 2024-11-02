# TypeHints Definition
Id = Annotated[int, Field(description="Any ID represented as a string.")]
SpaceTitle = Annotated[str, Field(descripton="A well-crafted space title.")]
BoardTitle = Annotated[str, Field(descripton="A well-crafted board title.")]

BoardDescription = Annotated[str, Field(descripton="A brief board description")]
SpaceDescription = Annotated[str, Field(descripton="A brief space description")]


# Models definition

class Space(BaseModel):
    id: Id
    title: SpaceTitle
    created: str
    updated: str
    external_id: Optional[str, None]
    description: SpaceDescription


class Board(BaseModel):
    id: Id
    title: BoardTitle
    created: str
    updated: str
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
    column_id	null	
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
