from fastapi import FastAPI

app = FastAPI()

@app.get("/items/", operation_id="12334", include_in_schema=False)
async def read_items():
    return [{"name": "Foo"}, {"name": "Bar"}]
