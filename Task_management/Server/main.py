from fastapi import FastAPI , Body , HTTPException
from pydantic import BaseModel

from Routes import Schedule_organizing_program as SOP

app = FastAPI()

class Task(BaseModel) :
    start_day : int = None 
    end_day : int = None
    prior : int = None 
    name : str = None 

@app.get("/schedule/check_list")
def check() :
    return SOP.check_list()

@app.delete("/schedule/delete_task")
def clear_current_tasks() :
    SOP.tasks.clear()
    return {"Tasks in Queue" : "None"}

@app.put("/schedule/update_task")
def update_task(id: str, change: Task):
    result = SOP.update_task(id, **change.model_dump(exclude_none=True))

    if result is None:
        raise HTTPException(status_code=404, detail=f"Not found task named {id}")
    if result is False:
        raise HTTPException(status_code=400, detail="Invalid start and finish day")
    return {"Message": "Task updated", "task": vars(result)}

@app.post("/schedule/insert")
def Receiving_task(task : Task) :
    if SOP.assign_task(task.start_day , task.end_day , task.prior , task.name) :
        return {"Message" : "Succesfully assign task"}
    else :
        raise HTTPException(status_code = 400 , detail = "Invalid input : Please review start and finish day")