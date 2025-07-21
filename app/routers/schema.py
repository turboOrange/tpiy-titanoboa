import strawberry
from app.routers.resolvers import Query, Mutation  # You'll define those

schema = strawberry.Schema(query=Query, mutation=Mutation)
