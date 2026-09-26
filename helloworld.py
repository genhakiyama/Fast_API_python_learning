from fastapi import FastAPI

app = FastAPI()
items = []

@app.get("/")
def root() :
    return {"hello , world"}

@app.post("/items")
def create_items(item : str) :
    items.append(item)
    return items