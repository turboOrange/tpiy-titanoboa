from sqlalchemy import Column, Integer, String
from ..database import Base


class Password(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    password = Column(String)
    tfa = Column(String, nullable=True)
    icon_url = Column(String, nullable=True)
    description = Column(String, nullable=True)
