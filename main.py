from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
@app.get("/")
async def read_root():
    return 'Here is my first FastApi request'


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/testing")
async def read_item_details(item:Item):
    result={"Name":item.name,"Price":item.price,"IsOffer":False}
    return result


