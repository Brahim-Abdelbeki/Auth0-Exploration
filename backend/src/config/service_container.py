from config.logging import logger

from models.services import Services

from services.user_service import UserService
from repositories.user_repository import UserPrismaRepository

class ServiceContainer:
    _instance: Services | None = None

    @classmethod
    def get_instance(cls) -> Services:
        if cls._instance is None:
            cls._instance = cls._initialize()
        return cls._instance

    @classmethod
    def _initialize(cls) -> Services:
        try:

            # init repos
            user_repo = UserPrismaRepository()

            # Init services
            user_service = UserService(user_repository=user_repo)

            logger.info(f"Main Agent services initialized successfully")

            return {
                "user": user_service,
            }
        except Exception as e:
            logger.error(
                f"Error initializing Main Agent services: {str(e)}", exc_info=True
            )
            raise