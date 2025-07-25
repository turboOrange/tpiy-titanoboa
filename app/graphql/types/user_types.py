from _typeshed import StrPath
import strawberry


@strawberry.type
class User:
    id: int
    name: str
    email: str


@strawberry.type
class AurhPayLoad:
    token: str
    user: User


@strawberry.type
class RegisterInput:
    name: str
    email: str
    password: str


@strawberry.type
class LoginInput:
    email: str
    password: str


@strawberry.type
class ChangeEmailInput:
    new_email: str
    token: str


@strawberry.type
class ChangeMasterPasswordInput:
    new_password: str
    old_password: str
    token: str


@strawberry.type
class ChangeNameInput:
    new_name: str
    token: str
