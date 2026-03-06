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
        user_answered_response = await poll_client.check_user_answered(request.user_id, request.question_id)
        print(user_answered_response)
        if user_answered_response["status_code"] == 400:
            raise ValueError (user_answered_response["data"])
        if user_answered_response["data"]:
            raise ValueError ("User already answered")
        else:
            if request.answer_id > 4 or request.answer_id < 0:
                raise ValueError('answer_id must be between 1 and 4')
            return await poll_client.answer_question(request)
    else:
        raise ValueError ("User needs to be registered")


async def update_answer(request : AnswerRequest)->Optional[int]:
    user : User = await user_repository.get_user_by_id(request.user_id)

    if user:
        if user.is_registered:
            user_answered_check = await poll_client.check_user_answered(user.id, request.question_id)
            if user_answered_check:
                if request.answer_id > 4 or request.answer_id < 1:
                    raise ValueError('answer_id must be between 1 and 4')
                return await poll_client.update_answer(request.question_id, request.answer_id, request.user_id)
            raise ValueError ("User hasn't answered this question yet, use answer question instead")
        raise ValueError("User needs to be registered")
    raise ValueError ("User doesn't exist")

async def delete_answer(user_id:int, question_id:int)->Optional[int]:
    user : User = await user_repository.get_user_by_id(user_id)
    if not user:
        raise ValueError("User not found")
    user_answered_check = await poll_client.check_user_answered(user_id, question_id)
    if user_answered_check["status_code"] == 400:
        raise ValueError (user_answered_check["data"])
    if user_answered_check["data"]:
        return await poll_client.delete_answer(user_id,question_id)
    else:
        raise ValueError ("User hasn't answered this question yet.")
