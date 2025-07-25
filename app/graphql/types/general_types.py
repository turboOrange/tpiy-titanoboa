import strawberry


@strawberry.type
class Message:
    success: bool
    message: str
