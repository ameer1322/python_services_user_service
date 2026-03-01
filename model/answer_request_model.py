from pydantic import BaseModel

class AnswerRequest(BaseModel):
    question_id:int
    answer_id:int
    user_id:int