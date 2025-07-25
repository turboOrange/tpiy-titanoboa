import strawberry
import os
from app.graphql.queries.password_query import PasswordQuery
from app.graphql.queries.user_query import UserQuery
from app.graphql.mutations.password_mutation import PasswordMutation
from add.graphql.mutations.user_mutation import UserMutation
from app.database import get_db
from fastapi import Depends


@strawberry.type
class Query(UserQuery, PasswordQuery):
    @strawberry.field
    def version(self) -> str:
        return os.getenv("VERSION") or "unspecified"


@strawberry.type
class Mutation(UserMutation, PasswordMutation):
    pass


schema = strawberry.Schema(query=Query, Mutation=Mutation)


def get_context(db=Depends(get_db)):
    return {"db": db}
