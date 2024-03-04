import functools
from datetime import datetime

import chromadb
from fastapi import FastAPI
from pydantic import BaseModel

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


class SimRequest(BaseModel):
    text: str


# put in function to ensure relative paths work
# TODO: fix this bug in future on mlrpc
# there will be as many copies as many workers so keep that in mind
@functools.lru_cache(maxsize=1)
def get_collection(path="data/chroma", name="test"):
    db = chromadb.PersistentClient(path=path)  # Initialize ChromaDB
    collection = db.get_or_create_collection(name=name)
    print_msg("Loading collection...")
    return collection


@app.post("/similarity")
def similarity(req: SimRequest):
    try:
        print_msg("Similarity calculation")
        return get_collection().query(query_texts=[req.text])
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
