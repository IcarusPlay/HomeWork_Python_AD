from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class CategoryBase(BaseModel):
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class CategoryCreate(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class QuestionCreate(BaseModel):
    text: str = Field(..., min_length=12)
    category_id: Optional[int] = None  # можно не указывать категорию


class QuestionResponse(BaseModel):
    id: int
    text: str
    category_id: Optional[int] = None
    category: Optional[CategoryResponse] = None

    model_config = ConfigDict(
        from_attributes=True
    )


class MessageResponse(BaseModel):
    message: str
