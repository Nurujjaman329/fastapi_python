from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str  # "customer" or "vendor"

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
