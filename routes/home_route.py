from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

home_router = APIRouter()

@home_router.get("/")
async def home():
    return  PlainTextResponse("Welcome to FastAPI Student-Subject API") 