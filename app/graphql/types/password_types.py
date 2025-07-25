import strawberry
from type import List


@strawberry.type
class PasswordEntry:
    id: int
    name: str
    user_name: str = strawberry.field(name="userName")
    password: str
    description: str
    tfa: str
    iconUrl: str


@strawberry.type
class PaginatedPasswordEntries:
    items: List[PasswordEntry]
    total_count: int = strawberry.field(name="totalCount")
    page: int
    page_size: int = strawberry.field(name="pageSize")
    has_next_page: bool = strawberry.field(name="hasNextPage")
