from fastapi import APIRouter


router = APIRouter(prefix='/user', tags=['User'])


@router.get('/hello', description="Send a hello message")
async def add_clients() -> dict:
    return {"message": "Hello, World!"}
    
@router.get('/hellos', description="Send a hello message")
async def add_clients() -> list[dict]:
    return [{"message": "Hello, World!"}]