from typing import TypedDict

from services.user_service import UserService

class Services(TypedDict):
    user: UserService