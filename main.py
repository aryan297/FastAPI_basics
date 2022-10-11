from typing import Union
from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel

fake_items_db = [{"item_name": "Foo",'item_id':1}, {"item_name": "Bar" ,'item_id':2}, {"item_name": "Baz",'item_id':3}]


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item": fake_items_db[item_id]}

@app.post('/items_add')
async def create_item(item:Item):
    return item
