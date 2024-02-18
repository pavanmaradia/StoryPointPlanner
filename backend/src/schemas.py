"""
Schema serializer
"""
import pydantic


class _UserBase(pydantic.BaseModel):
    email: str


class UserCreate(_UserBase):
    password: str

    class Config:
        orm_mode = True


class User(_UserBase):
    id: int

    class Config:
        orm_mode = True
