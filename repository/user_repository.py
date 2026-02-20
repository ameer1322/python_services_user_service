from typing import Optional, List

import json
from repository.database import database
from model.user_model import User


async def create_user(user : User) :
    query = """
        INSERT INTO users (first_name, last_name, email, age, address) 
        VALUES (:first_name, :last_name, :email, :age, :address)
        """

    values = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }

    async with database.transaction():
        await database.execute(query, values=values)
        last_record_id = await database.fetch_one("SELECT LAST_INSERT_ID()")

    return last_record_id[0]

async def get_user_by_id(user_id: int) -> Optional[User]:
    query = """
    SELECT * FROM users WHERE id = :id
            """
    values = {
        "id": user_id
    }
    async with database.transaction():
        return await database.fetch_one(query, values=values)


async def delete_user(user_id: int) -> User:
    query = """
    DELETE FROM users WHERE id = :id
    """
    values = {
        "id": user_id
    }
    async with database.transaction():
        deleted_user = await database.fetch_one("SELECT * FROM users WHERE id = :id", values=values)
        await database.execute(query, values=values)
    return deleted_user

async def update_user(user: User) -> User:
    query = """
    UPDATE users
    SET first_name = :first_name, 
    last_name = :last_name, 
    email = :email, 
    age = :age, 
    address = :address
    WHERE id = :id
    """
    values = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "age": user.age,
        "address": user.address
    }
    async with database.transaction():
        await database.execute(query, values=values)
        return user

