from interfaces.user_interface import IUserRepository
from config.logging import logger
from models.user import User

class UserService:
    def __init__(self, user_repository: IUserRepository):
        self.repo = user_repository

    async def add_user(self, user: User):
        user = await self.repo.add_user(user=user)
        logger.info(f"User {user.name} created successfully")