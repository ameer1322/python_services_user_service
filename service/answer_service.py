from typing import Optional, List

from model.answer_request_model import AnswerRequest
from model.delete_request_model import DeleteRequest
from model.user_model import User

from repository import user_repository

from clients import poll_client


async def answer_question(request : AnswerRequest)-> Optional[int]:
    user : User = await user_repository.get_user_by_id(request.user_id)
    if not user:
        raise ValueError("User not found")
    if user.is_registered:
        user_answered_check = await poll_client.check_user_answered(request.user_id, request.question_id)
        if user_answered_check:
            raise ValueError ("User already answered question, use update answer instead")
        else:
            return await poll_client.answer_question(request)
    else:
        raise ValueError ("User needs to be registered")


async def update_answer(request : AnswerRequest)->Optional[int]:
    user : User = await user_repository.get_user_by_id(request.user_id)
    if user.is_registered:
        user_answered_check = await poll_client.check_user_answered(user.id, request.question_id)
        if user_answered_check:
            return await poll_client.update_answer(request.question_id, request.answer_id, request.user_id)
        else:
            raise ValueError ("User hasn't answered this question yet, use answer question instead")
    else:
        raise ValueError ("User needs to be registered")

async def delete_answer(user_id:int, question_id:int)->Optional[int]:
    user_answered_check = await poll_client.check_user_answered(user_id, question_id)
    if user_answered_check:
        return await poll_client.delete_answer(user_id,question_id)
    else:
        raise ValueError ("User hasn't answered this question yet.")