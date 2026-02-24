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
    return await user_repository.delete_user(user_id)

async def update_user(user: User) -> User:
    return await user_repository.update_user(user)

