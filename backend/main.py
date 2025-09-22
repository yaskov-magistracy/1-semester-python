from fastapi import FastAPI
from api.endpoints.Routes import apiRouters
import uvicorn
import dramatiq
from dramatiq.brokers.redis import RedisBroker 
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from dramatiq.brokers.stub import StubBroker

app = FastAPI()
app.include_router(apiRouters)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


broker = StubBroker()
redisBroker = RedisBroker(host="localhost", port=6379)

dramatiq.set_broker(broker)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

