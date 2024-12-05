from motor.motor_asyncio import AsyncIOMotorClient
from .config import get_settings

settings = get_settings()

class Database:
    client: AsyncIOMotorClient = None
    
    def get_client(self) -> AsyncIOMotorClient:
        return self.client
    
    def get_db(self):
        return self.client[settings.MONGO_DB]
    
    async def connect(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URL)
        
    async def disconnect(self):
        if self.client:
            self.client.close()
            self.client = None


db = Database()
