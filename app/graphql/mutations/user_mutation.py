from os import name
import jwt
import datetime

from app.crud.user_crud import UserCrud
from app.graphql.types.general_types import Message
from app.graphql.types.user_types import (
    LoginInput,
    RegisterInput,
    ChangeMasterPasswordInput,
    ChangeEmailInput,
    ChangeNameInput,
)
import strawberry
import secrets


@strawberry.type
class UserMutation:
    @strawberry.mutation
    def login_user(self, input: LoginInput, info) -> User:
        db = info.context["db"]

    @strawberry.mutation
    def register_user(self, input: RegisterInput, info) -> Message:
        db = info.context["db"]
        UserCrud.create_user(db, name=input.email, password=input.password, name=input.name, salt=secrets.token_bytes(16))
        return Message(success=True, message="User registered successfully.")
        

    @strawberry.mutation
    def change_master_password(self, input: ChangeMasterPasswordInput, info) -> Message:
        db = info.context["db"]

    @strawberry.mutation
    def change_email(self, input: ChangeEmailInput, info) -> Message:
        db = info.context["db"]

    @strawberry.mutation
    def change_name(self, input: ChangeNameInput, info) -> Message:
        db = info.context["db"]
