from schemas.message import Message


def Success(detail: str) -> Message:
    return Message(detail=detail)