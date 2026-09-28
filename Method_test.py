from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item (BaseModel) :
    start_day : int 
    end_day : int
    valuation : int 
    is_done : bool = False 

    def valid(self) :
        if (self.start_day > self.end_day) : 
            return False 

        return True

items = []

@app.post("/schedule/task_insert" , response_model=list[Item])
def Receiving_Request(item : Item) :
    if item.valid() :
        items.append(item)
        # return "Your schedule before adjusting : \n {items}"
        return items
    else :
        raise HTTPException(status_code = 400 , detail = "Bad Request : Invalid input")


@app.put("/schedule/task_adjust")
def Update_input(item_id : int , new_val : Item) :
    if (item_id < len(items)) :
        items[item_id] = new_val
        return items
    else :
        raise HTTPException(status_code = 400 , detail = "Bad Request : Invalid input") 
    
@app.delete("/schedule")
def Clear_list():
    items.clear()
    return items