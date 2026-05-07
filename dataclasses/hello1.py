from dataclasses import field
from fastapi import FastAPI
from pydantic.dataclasses import dataclass

@dataclass
class Item:
    name: str
    description: str | None = None

@dataclass
class Author:
    name: str
    items: list[Item] = field(default_factory=list)

app = FastAPI()

@app.post("/authors/{author_id}/items", response_model=Author)
async def create_author_items(author_id: str, item: list[Item]):
    return {"name": author_id, "items": item}


@app.get("/authors", response_model=list[Author])
async def get_authors():
    return [
        {
            "name": "Author 1",
            "items": [
                {"name": "Item 1", "description": "Description 1"},
                {"name": "Item 2"},
            ],
            
        },
        {
            "name": "Author 2",
            "items": [
                {"name": "Item 3", "description": "Description 3"},
                {"name": "Item 4"},
            ],
        }
    ]