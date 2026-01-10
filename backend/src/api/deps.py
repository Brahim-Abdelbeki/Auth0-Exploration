from services.user_service import UserService
from config.service_container import ServiceContainer

async def get_user_service() -> UserService:
    services = ServiceContainer.get_instance()
    return services["user"]