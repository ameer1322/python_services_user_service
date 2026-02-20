from typing import Optional, List

from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.functions import user
from starlette import status

from model.user_model import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User) :
    try:
        await user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/user_id/{user_id}", status_code=status.HTTP_200_OK)
async def read_users(user_id: int) -> Optional[User] :
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/{user_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: User) -> User:
    try:
        await user_service.update_user(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int) -> User:
    try:
        deleted_user =await user_service.delete_user(user_id)
        return deleted_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

