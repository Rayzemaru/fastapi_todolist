from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List



class Person(BaseModel):
    firstname: str
    lastname: str

people = [
    Person(
        firstname="Дмитро",
        lastname="Бебих"
    ),
    Person(
        firstname="Сергій",
        lastname="Папіровий"
    )
]

# Define a router for the Person resource
router = APIRouter()

@router.get("/people", response_model=List[Person])
def get_people():
    return people

@router.get("/people/{firstname}", response_model=Person)
def get_person(firstname: str):
    for person in people:
        if person.firstname == firstname:
            return person
    return {"error": "Person not found"}

@router.post("/people", response_model=Person)
def add_person(person: Person):
    people.append(person)
    return person
