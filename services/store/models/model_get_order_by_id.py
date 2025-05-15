from enum import Enum
from datetime import datetime
from pydantic import BaseModel

class OrderStatus(str, Enum):
    placed = "placed"
    approved = "approved"
    delivered = "delivered"

class ApiResponse(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: datetime
    status: OrderStatus
    complete: bool