import chromadb

if __name__ == "__main__":
    db = chromadb.PersistentClient(path="data/chroma")
    # generate random sentences
    sentences = ["This is a test sentence", "Another example sentence"]
    collection = db.get_or_create_collection(name="test")
    ids = []
    documents = []
    for i, embedding in enumerate(sentences):
        ids.append(f"id_{i}")
        documents.append(embedding)

    collection.upsert(ids=ids, documents=documents)
