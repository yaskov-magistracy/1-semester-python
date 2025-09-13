from fastapi import FastAPI, HTTPException, Response, status
from api.endpoints.routes import apiRouters
import uvicorn
from pydantic import BaseModel

app = FastAPI()
app.include_router(apiRouters)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

## TODO: move in Api folder