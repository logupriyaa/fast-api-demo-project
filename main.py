from fastapi import FastAPI
from model import Task
from fastapi import HTTPException

app = FastAPI()

tasks = []


@app.get("/")
def home():
    return {"message": "Welcome to Task manager"}

@app.post("/tasks/")
def create_task(task:Task):
    tasks.append(task)
    return {"messsage": "Task created", "task": task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):
    tasks[task_id] = updated_task
    return {"message": "Task updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks.pop(task_id)
    return {"message": "Task deleted"}