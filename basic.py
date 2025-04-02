from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

items = []

class Item(BaseModel):
    text: str = None
    is_done: bool = False


@app.get('/')
def root():
    return {'hello':'world'}

@app.post('/items')
def create_item(item:Item):
    items.append(item)
    return items

@app.get('/items/{item_limit}')
def get_limit(item_limit:int):
    return items[:item_limit]

@app.get('/items/{items_id}')
def get_item(items_id:int) -> Item:
    if items_id < len(items):
        item =  items[items_id]
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {items_id} Not Found")