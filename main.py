import uvicorn
from fastapi import FastAPI, HTTPException
from models import Item

app = FastAPI(
    title="Building High-Performance APIs with FastAPI and Pydantic",
    description="This is a simple example of building high-performance APIs with FastAPI and Pydantic",
    # version="2.0.0"
)

items = {}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id in items:
        return items[item_id]
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id in items:
        items[item_id] = item
        return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    if item_id in items:
        return items.pop(item_id)
    raise HTTPException(status_code=404, detail="Item not found")



if __name__ == '__main__':
    # configure()
    uvicorn.run(app, port=8000, host='127.0.0.1')
