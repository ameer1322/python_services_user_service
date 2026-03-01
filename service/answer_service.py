from typing import Optional, List

from model.answer_request_model import AnswerRequest
from model.user_model import User

from repository import user_repository

from clients import poll_client


async def answer_question(request : AnswerRequest):
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


async def update_answer(question_id : int, answer_id:int, user: User):
    if user.is_registered:
        user_answered_check = await poll_client.check_user_answered(user.id, question_id)
        if user_answered_check:
            return await poll_client.update_answer(question_id, answer_id, user)
        else:
            return "User hasn't answered this question yet, use answer question instead"
    else:
        return "User needs to be registered"