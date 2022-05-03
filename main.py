from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(),
        first_name="Alex",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]
@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;