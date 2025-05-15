from pydantic import BaseModel

class ApiResponse(BaseModel):
    approved: int
    placed: int
    delivered: int