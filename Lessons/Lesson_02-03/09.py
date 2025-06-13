from datetime import datetime

from pydantic import BaseModel, EmailStr, HttpUrl, Field
from decimal import Decimal


class Product(BaseModel):
    name: str
    price: Decimal
    tags: list[str]


class User(BaseModel):
    full_name: str
    age: int
    email: EmailStr
    homepage: HttpUrl # https://
    # products: list[Product] = []  # WRONG!!!!
    products: list[Product] = Field(default_factory=list)
    created_at: datetime

    # model_config = DictSchema()

    class Config:
        str_strip_whitespace = True
        validate_assignment = True
        json_encoders = {
            datetime: lambda value: value.strftime("%d-%m-%Y %H:%M")
        }


user = User(
    full_name="J. Johanson",
    age=32,
    email="j.johanson@google.com",
    homepage="https://example.com"
)

print(user)