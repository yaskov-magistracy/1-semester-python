from fastapi import FastAPI
from api.endpoints.Routes import apiRouters
import uvicorn
import dramatiq
from dramatiq.brokers.redis import RedisBroker 
from config import settings

app = FastAPI()
app.include_router(apiRouters)

dramatiq.set_broker(RedisBroker(
    host=settings.REDIS_HOST(), 
    port=settings.REDIS_PORT(), 
    db=0, 
    password=settings.REDIS_PASSWORD()))

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
