from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, Login, Token
from app.services.auth_service import AuthService
from app.database import get_db
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register(user)

@router.post("/login", response_model=Token)
def login(user: Login, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(user)

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
