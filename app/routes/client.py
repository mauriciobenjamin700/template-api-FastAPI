from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session



router = APIRouter(prefix='/client', tags=['Client'])

@router.post('/add', description="add new client")
async def add_clients(
) -> dict:
    result = {"mensage": "Client added!"}
    
