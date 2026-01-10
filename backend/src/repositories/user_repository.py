from db.prisma.database import db
from interfaces.user_interface import IUserRepository
from config.logging import logger
from models.user import User

class UserPrismaRepository(IUserRepository):
    async def add_user(self, user: User):
        await db.connect()

        try:
            return await db.user.create(
                data={
                    "id": user.userid,
                    "email": user.email,
                    "name": user.name
                }
            )
        except Exception as e:
            logger.error(f"Error creating user {user.name}: {str(e)}", exc_info=True)
            raise


