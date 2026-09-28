from fastapi import FastAPI , Body , HTTPException
from pydantic import BaseModel

from Routes import Schedule_organizing_program as SOP

app = FastAPI()

class Task(BaseModel) :
    start_day : int 
    end_day : int 
    prior : int 
    name : str 

@app.get("/schedule/check_list")
def check() :
    return SOP.check_list()

@app.delete("/schedule/delete_task")
def clear_current_tasks() :
    SOP.tasks.clear()
    return {"Tasks in Queue" : "None"}

@app.post("/schedule/insert")
def Receiving_task(task : Task) :
    if SOP.assign_task(task.start_day , task.end_day , task.prior , task.name) :
        return {"Message" : "Succesfully assign task"}
    else :
        raise HTTPException(status_code = 400 , detail = "Invalid input : Please review start and finish day")
