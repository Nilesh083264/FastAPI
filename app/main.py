from fastapi import FastAPI, HTTPException, Depends
import uvicorn
# from database import SessionLocal, engine, Base
from api.routes import router as api_routers
from core.config import settings


app1 = FastAPI()
app1.include_router(api_routers)


if __name__ == "__main__":
    uvicorn.run("main:app1", host=settings.HOST, port=settings.PORT)
