from pydantic import BaseModel

class DeleteRequest(BaseModel):
    user_id : int
    question_id : int