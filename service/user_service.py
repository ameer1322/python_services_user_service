from typing import Optional, List

from config.config import  Config

from model.user_model import User

from repository import user_repository

from clients import poll_client

import httpx

POLL_SERVICE_URL = Config.POLL_SERVICE_BASE_URL

async def create_user(user: User) -> User:
    return await user_repository.create_user(user)

async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)

async def delete_user(user_id: int) -> User:
    return await user_repository.delete_user(user_id)

async def update_user(user: User) -> User:
    return await user_repository.update_user(user)

async def answer_question(question_id : int, answer_id:int, user: User):
    if user.is_registered:
        return await poll_client.answer_question(question_id,answer_id,user)
    else:
        return "User needs to be registered"

