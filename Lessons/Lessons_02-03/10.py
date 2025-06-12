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