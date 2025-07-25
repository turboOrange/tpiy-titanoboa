# app/main.py
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from graphql.schema import schema, get_context
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmake

load_dotenv()
app = FastAPI(
    title="tpiy-titanoboa",
    version=os.getenv("VERSION") or "unspecified",
    description="GraphQL API for managing items and users",
)

# CORS (adjust for your frontend)
# app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
# )

# Create GraphQL router and include it
graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/graphql")


# Optional health check
@app.get("/health")
def health_check():
    return {"status": "ok"}
