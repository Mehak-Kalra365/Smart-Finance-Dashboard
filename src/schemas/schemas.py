from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "admin"
    ANALYST = "analyst"
    VIEWER = "viewer"

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.VIEWER

class UserResponse(UserBase):
    id: int
    role: UserRole

    class Config:
        orm_mode = True
        from_attributes = True

class RecordBase(BaseModel):
    amount: float = Field(gt=0)
    type: TransactionType
    category: str
    notes: Optional[str] = ""

class RecordCreate(RecordBase):
    pass

class RecordResponse(RecordBase):
    id: int
    user_id: int
    date: datetime

    class Config:
        orm_mode = True
        from_attributes = True