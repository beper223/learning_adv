from pydantic import (
    BaseModel, EmailStr,
    HttpUrl, Field,
    field_validator, ConfigDict,
    model_validator
)
from decimal import Decimal
import typing
from datetime import datetime

from pydantic_core.core_schema import DictSchema


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

# NEW VARIANT (pydantic v2)
    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda value: value.strftime("%d-%m-%Y %H:%M")
        }
    )

# OLD VARIANT (pydantic v1)
    # class Config:
    #     str_strip_whitespace = True
    #     validate_assignment = True # позволяет валидировать уже созданные объекты (обновление данных)
    #     json_encoders = {
    #         datetime: lambda value: value.strftime("%d-%m-%Y %H:%M")
    #     }

    @field_validator('email') # ...@example.com | gmail.com
    def validate_email(cls, value: str) -> str:
        # test.email@gmail.com + split("@") -> ['test.email', 'gmail.com'] + [-1] -> gmail.com
        allowed_domains = {'example.com', 'gmail.com'}
        email_domain = value.split("@")[-1]

        if email_domain not in allowed_domains:
            raise ValueError(f"Email must be from one of allowed domains: {', '.join(allowed_domains)}")

        return value


user = User(
    full_name="J. Johanson",
    age=32,
    email="j.johanson@gmail.com",
    homepage="https://example.com",
    created_at=datetime(year=2023, month=5, day=21, hour=15, minute=42)
)


print(user)

print(user.model_dump_json(indent=4))

# user.email = "j.johanson@mail.ru"
# print(user)

# def foo(data: list | None = None):
#     if not data:
#         data = []
#
#     ...


def process_user_input(data):
    ...