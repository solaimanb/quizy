from fastapi import FastAPI
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

temp_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

items = [
    {"item_id": "1", "name": "Item 1"},
    {"item_id": "2", "name": "Item 2"},
    {"item_id": "3", "name": "Item 3"},
    {"item_id": "4", "name": "Item 4"},
    {"item_id": "5", "name": "Item 5"},
]

@app.get("/")
def root():
    return {"QUIZY"}

@app.get("/quizes/{item_id}")
async def read_quiz(item_id: int | float):
    return {"Quiz": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# Query Parameters: http://localhost:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return temp_items_db[skip : skip + limit]

# Optional Parameters: http://localhost:8000/items/optional/?skip=0&limit=10
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)