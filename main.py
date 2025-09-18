from fastapi import FastAPI
from api.endpoints.Routes import apiRouters
import uvicorn

app = FastAPI()
app.include_router(apiRouters)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
