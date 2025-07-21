# app/main.py

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.routers.schema import schema  # Define your Strawberry schema here
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="GraphQL API",
    version="1.0.0",
    description="GraphQL API for managing items and users",
)

# CORS (adjust for your frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create GraphQL router and include it
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


# Optional health check
@app.get("/health")
def health_check():
    return {"status": "ok"}
