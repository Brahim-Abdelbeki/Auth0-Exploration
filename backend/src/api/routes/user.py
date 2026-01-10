from ..deps import get_user_service
from services.user_service import UserService
from models.user import User
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("")
async def add_user(user: User, user_service: UserService = Depends(get_user_service)):
    user = await user_service.add_user(user=user)
    return user
