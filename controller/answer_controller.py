from logging import exception
from typing import Optional, List

from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.functions import user
from starlette import status

from model.user_model import User
from service import user_service, answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"],
)

@router.post("/answer_question",status_code=status.HTTP_200_OK)
async def answer_question(question_id:int,answer_id:int,user:User):
    try:
        await answer_service.answer_question(question_id,answer_id,user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.put("/update_answer",status_code=status.HTTP_200_OK)
async def update_answer(question_id:int,answer_id:int,user:User):
    try:
        await answer_service.update_answer(question_id,answer_id,user)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
