from logging import exception
from typing import Optional, List

from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.functions import user
from starlette import status

from model.delete_request_model import DeleteRequest
from model.user_model import User
from model.answer_request_model import  AnswerRequest
from service import user_service, answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"],
)

@router.post("/",status_code=status.HTTP_201_CREATED)
async def answer_question(request : AnswerRequest):
    try:
        return await answer_service.answer_question(request)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.put("/",status_code=status.HTTP_200_OK)
async def update_answer(request : AnswerRequest):
    try:
        return await answer_service.update_answer(request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.delete("/user/{user_id}/question/{question_id}",status_code=status.HTTP_200_OK)
async def delete_answer(user_id : int, question_id: int):
    try:
        return await answer_service.delete_answer(user_id, question_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))