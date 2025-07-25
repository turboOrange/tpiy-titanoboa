from os import name
import jwt
import datetime


from app.graphql.types.general_types import Message
from app.graphql.types.user_types import LoginInput, RegisterInput, ChangeMasterPasswordInput, ChangeEmailInput, ChangeNameInput
import strawberry

@strawberry.type
class UserMutation:
    @strawberry.mutation
    def login_user(self, input: LoginInput) -> Message:
        pass

    @strawberry.mutation
    def register_user(self, input: RegisterInput) -> User:
        pass

    @strawberry.mutation
    def change_master_password(self, input: ChangeMasterPasswordInput) Message:
        pass

    @strawberry.mutation
    def change_email(self, input: ChangeEmailInput) -> Message:
        pass

    @strawberry.mutation
    def change_name(self, input: ChangeNameInput) -> Message:
        class
