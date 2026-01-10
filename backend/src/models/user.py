from pydantic import BaseModel, EmailStr

class User(BaseModel):
    userid: int
    email: EmailStr
    name: str