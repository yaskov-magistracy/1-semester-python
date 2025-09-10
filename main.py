from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

@app.get("/asd")
def root():
    return "Asd123"

@app.get("/asd/{id}",
         tags=["Тестовый заголовок"],
         summary="Тестирование апихи")
def test(id: int):
    if id == 1:
        return ""
    raise HTTPException(404, "Ошибочка")

class TestEntity(BaseModel):
    integer: int
    string: str

entities = []


@app.post("/add")
def testPost(testEntity: TestEntity) -> int:
    entities.append(testEntity)