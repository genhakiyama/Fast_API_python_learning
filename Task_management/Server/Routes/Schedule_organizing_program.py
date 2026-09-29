from collections import deque

class Task :
    def __init__(self , start : int , finish : int , prior : int , id : str , is_done : str = "In Queue") :
        self.start_day = start 
        self.end_day = finish 
        self.prior = prior 
        self.id = id 
        self.status = is_done 

    def valid(self) -> bool :
        if self.start_day > self.end_day :
            return False 
        return True 

tasks = []

def process() :
    tasks.sort(key = lambda x : (x.prior , x.start_day , x.end_day) , reverse = True)

def find(id : str) :
    for x in tasks :
        if x.id == id :
            return x
    return None 

def update_task(id : str , start_day = None , end_day = None , prior = None , name = None) :
    task = find(id)
    if task is None :
        return None 
    old_task = {task.start_day , task.end_day , task.prior , task.status}

    if start_day is not None : task.start_day = start_day
    if end_day is not None : task.end_day = end_day
    if prior is not None : task.prior = prior
    if name is not None : task.status = name

    if not task.valid() :
        task.start_day , task.end_day , task.prior , task.status = old_task
        return False 
    process()
    return task

def assign_task(start_day : int , end_day : int , priority : int , name_task : str) :
    task = Task(start_day , end_day , priority , name_task)
    if task.valid() :
        tasks.append(task)
        return True 
    else :
        return False 

def check_list() :
    process()
    if not tasks :
        return "No task left in Queue"
    else :
        return tasks
    

