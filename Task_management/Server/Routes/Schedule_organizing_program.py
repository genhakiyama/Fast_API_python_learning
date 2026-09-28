from collections import deque
from pydantic import BaseModel

# class Task(BaseModel) :  -- using BaseModel method
#     start_day : int 
#     end_day : int 
#     prior : int 
#     id : str 
#     is_done : bool = False 

#     def valid(self) -> bool :
#         if self.start_day > self.end_day :
#             return False 
#         return True 

class Task :
    def __init__(self , start : int , finish : int , prior : int , id : str , is_done = False) :
        self.start_day = start 
        self.end_day = finish 
        self.prior = prior 
        self.id = id 
        self.is_done = is_done 

    def valid(self) -> bool :
        if self.start_day > self.end_day :
            return False 
        return True 

tasks = []

def assign_task(start_day : int , end_day : int , priority : int , name_task : str) :
    task = Task(start_day , end_day , priority , name_task)
    if task.valid() :
        tasks.append(task)
        return True 
    else :
        return False 

def process() :
    tasks.sort(key = lambda x : (x.prior , x.start_day , x.end_day) , reverse = True)

def check_list() :
    process()
    if not tasks :
        return "No task left in Queue"
    else :
        return tasks
    

