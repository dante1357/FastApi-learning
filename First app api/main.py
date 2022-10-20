from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import User, Gender, Role
app = FastAPI()

db: List[User] = [
    User(
        id=UUID("26c25a1b-b4fe-4337-8204-8b6b53900e66"),
        first_name="mansoor",
        last_name="masoudi",
        user_name="dante1357",
        gender=Gender.male,
        roles=[Role.admin]
    ),
    User(
        id=uuid4(),
        first_name="Negin",
        last_name="Masoumzade",
        user_name="negin1372",
        gender=Gender.female,
        roles=[Role.user, Role.student]
    )
]


@app.get("/")
async def root():
    return {"Hello": "Mansoor"}


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exists"
        )
