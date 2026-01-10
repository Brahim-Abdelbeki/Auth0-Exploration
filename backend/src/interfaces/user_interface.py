from abc import ABC, abstractmethod
from models.user import User

class IUserRepository(ABC):
    @abstractmethod
    async def add_user(self, user: User):
        pass
