from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, Login
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_token import create_access_token
from fastapi import HTTPException, status

class AuthService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def register(self, user: UserCreate):
        existing_user = self.repo.get_by_email(user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        hashed_pw = hash_password(user.password)
        return self.repo.create(user, hashed_pw)

    def login(self, user: Login):
        db_user = self.repo.get_by_email(user.email)
        if not db_user or not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")
        token = create_access_token({"user_id": db_user.id})
        return {"access_token": token, "token_type": "bearer"}
