from prisma import Prisma
import threading

class DBClient:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DBClient, cls).__new__(cls)
                    cls._instance.prisma = Prisma()
        return cls._instance

    async def connect(self):
        await self.prisma.connect()

    async def disconnect(self):
        await self.prisma.disconnect()

db: Prisma = DBClient().prisma
