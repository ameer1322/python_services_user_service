
from model.user_model import User

import httpx

POLL_SERVICE_URL = "http://localhost:8001"

async def answer_question(question_id : int, answer_id:int, user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{POLL_SERVICE_URL}/answer_question",
            json={"question_id":question_id,"answer_id":answer_id,"user_id":user.id}
        )
        response.raise_for_status()
        return response.json()

async def update_answer(question_id:int, answer_id:int, user:User):
    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"{POLL_SERVICE_URL}/update_question",
            json={"question_id":question_id,"answer_id":answer_id,"user_id":user.id}
        )
        response.raise_for_status()
        return response.json()

async def check_user_answered(user_id:int, question_id:int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{POLL_SERVICE_URL}/check_user_answered/{user_id}/{question_id}"
        )
        response.raise_for_status()
        return response.json()
