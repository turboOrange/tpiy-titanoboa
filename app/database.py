from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from typing import Generator


engine = create_engine(
    os.environ.get("QLALCHEMY_DATABASE_URL"), connect_args={"check_same_thread": False}
)  # `check_same_thread` is needed for SQLite
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
