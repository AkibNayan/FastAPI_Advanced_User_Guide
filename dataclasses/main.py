from dataclasses import dataclass
from fastapi import FastAPI

app = FastAPI()

@dataclass
class Item:
    name: str
    price: float
    description: str | None = None
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    return item
