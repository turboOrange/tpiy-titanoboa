from sqlalchemy.orm import Session
from ..models.user import User


class UserCrud:
    @staticmethod
    def create_user(
        db: Session, name: str, email: str, password: str, salt: str
    ) -> User:
        db_user = User(name=name, email=email, password=password, salt=salt)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
