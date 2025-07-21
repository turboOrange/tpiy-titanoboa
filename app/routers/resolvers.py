import strawberry
from app.schemas.item import ItemOut


@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello, GraphQL!"

    # Example: get one item
    # @strawberry.field
    # async def item(self, id: int) -> ItemOut:
    #     return await get_item_by_id(id)


@strawberry.type
class Mutation:
    @strawberry.field
    def ping(self) -> str:
        return "pong"
