
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


# User registration request
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


# User response
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# Login request
class UserLogin(BaseModel):
    username: str
    password: str


# Expense creation request
class ExpenseCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=50)
    description: Optional[str] = None


# Expense update request
class ExpenseUpdate(BaseModel):
    title: Optional[str] = Field(
        default=None, min_length=1, max_length=100
    )
    amount: Optional[float] = Field(default=None, gt=0)
    category: Optional[str] = Field(
        default=None, min_length=1, max_length=50
    )
    description: Optional[str] = None


# Expense response
class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    description: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
