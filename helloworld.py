from fastapi import FastAPI
from fastapi import Body

app = FastAPI()
items = []

@app.get("/")
def root() :
    return {"hello , world"}

@app.post("/test1")
def create_items(item : str = Body(embed=True)) :
    items.append(item)
    return items

