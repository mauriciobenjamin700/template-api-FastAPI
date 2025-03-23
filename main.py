import asyncio
import uvicorn

from app.db.configs.connection import db
from app.server import app

async def create_tables():
    await db.create_tables()

if __name__ == "__main__":
    asyncio.run(create_tables())
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )