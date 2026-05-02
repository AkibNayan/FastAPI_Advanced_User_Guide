from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post("/items")
async def create_item(item: Item):
    return item

@app.get("/items1")
async def read_item() -> list[Item]:
    return [
        Item(name="Foo", price=45.2, tax=3.2, tags=["Bar", "Baz"]),
        Item(name="Baz", description="An optional description", price=102.3, tax=19.5, tags=["Bar", "Baz"])
    ]


@app.get("/items2", response_class= HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
