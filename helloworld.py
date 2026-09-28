from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
items = []

@app.get("/")
def root() :
    return {"hello , world"}

@app.post("/items")
def create_items(item : str) :
    items.append(item)
    return items

@app.get("/test1")
def root() :
    return {"test"}

@app.post("/test1")
def create_items(item : str = Body(embed=True)) :
    items.append(item)
    return items

