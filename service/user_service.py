from typing import Optional, List


from model.user_model import User

from repository import user_repository


async def get_users()->List[User]:
    return await user_repository.get_users()

async def create_user(user: User) -> User:
    return await user_repository.create_user(user)

async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)

async def delete_user(user_id: int) -> User:
    user_exists = await get_user_by_id(user_id)
    if user_exists:
        return await user_repository.delete_user(user_id)
    raise ValueError("User doesn't exist.")

async def update_user(user: User, user_id:int) -> User:
    user_exists = await get_user_by_id(user_id)
    if user_exists:
        return await user_repository.update_user(user,user_id)
    raise ValueError("User doesn't exist.")

async def register_user(user_id):
    return await user_repository.register_user(user_id)


async def is_registered(user_id):
    user_exists = await get_user_by_id(user_id)
    if user_exists:
        return await user_repository.is_registered(user_id)
    raise ValueError("User doesn't exist")