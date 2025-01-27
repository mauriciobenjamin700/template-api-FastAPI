from fastapi import APIRouter


from schemas.message import Message


router = APIRouter(prefix='/client', tags=['Client'])


@router.get('/hello', description="Send a hello message")
async def add_clients(
) -> Message:
    return Message(message="Hello, World!")
    
