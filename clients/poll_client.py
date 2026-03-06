from model.answer_request_model import AnswerRequest
from model.delete_request_model import DeleteRequest
from model.user_model import User

import httpx

POLL_SERVICE_URL = "http://localhost:8001"

async def answer_question(request: AnswerRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{POLL_SERVICE_URL}/answer/",
            json={"question_id":request.question_id,"answer_id":request.answer_id,"user_id":request.user_id}
        )
        data = None
        if response.content:
            data = response.json()
        return {
            "status_code": response.status_code,
            "data": data
        }

async def update_answer(question_id:int, answer_id:int, user_id:int):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{POLL_SERVICE_URL}/answer/update_answer",
            json={"question_id":question_id,"answer_id":answer_id,"user_id":user_id}
        )
        return {
            "status_code": response.status_code,
            "data": response.json()
        }

async def delete_answers_by_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{POLL_SERVICE_URL}/answer/delete_user_answers/{user_id}"
        )
        return {
            "status_code": response.status_code,
            "data": response.json()
        }

async def check_user_answered(user_id:int, question_id:int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{POLL_SERVICE_URL}/answer/check_user_answered/{user_id}/{question_id}"
        )
        return {
            "status_code": response.status_code,
            "data": response.json()
        }

async def delete_answer(user_id:int, question_id:int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{POLL_SERVICE_URL}/answer/delete_answer/user/{user_id}/question/{question_id}"
        )
        return {
            "status_code": response.status_code,
            "data": response.json()
        }