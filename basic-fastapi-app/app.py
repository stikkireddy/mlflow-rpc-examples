from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel

from some_module import foo

app = FastAPI()


def print_msg(msg):
    ts = datetime.utcnow()
    print(f"[{str(ts)}] {msg}", flush=True)


@app.get("/")
def read_root():
    print_msg("Hello World")
    return {
        "Hello": f"World",
    }


@app.post("/dev")
def read_root(data: str):
    return {"Hello": "test", "data": data}


@app.get("/dev")
def read_users(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}


@app.get("/demo")
def load_from_sample():
    return {"result": foo()}


@app.get("/demo/{item_id}/")
def load_from_sample(item_id: int):
    return {"result": foo(), "item_id": item_id}


class Item(BaseModel):
    name: str
    description: str = None


@app.post("/")
def create_item(item: Item):
    item.description = item.description.upper()
    return item
