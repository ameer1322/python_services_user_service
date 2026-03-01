from logging import exception
from typing import Optional, List

from fastapi import APIRouter, HTTPException
from sqlalchemy.sql.functions import user
from starlette import status

from model.user_model import User
from model.answer_request_model import  AnswerRequest
from service import user_service, answer_service

router = APIRouter(
    prefix="/answer",
    tags=["answer"],
)

@router.post("/answer_question",status_code=status.HTTP_201_CREATED)
async def answer_question(request : AnswerRequest):
    try:
        await answer_service.answer_question(request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@router.put("/update_answer",status_code=status.HTTP_200_OK)
async def update_answer(request : AnswerRequest):
    try:
        await answer_service.update_answer(request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))
