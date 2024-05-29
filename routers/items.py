from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List



class Task(BaseModel):
    title: str

tasks = [
    {"title": "Постригти Поліщу"},
    {"title": "За бажанням не бити Богдана"},
    {"title": "Кохати кицьку Танюшку"}
]

# Define a router for the tasks resource
router = APIRouter()

@router.post("/tasks", response_model=List[Task])
def add_tasks(new_task: Task):
    tasks.append(new_task)
    return tasks

@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

