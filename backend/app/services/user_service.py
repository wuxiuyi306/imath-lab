from typing import Optional
from bson import ObjectId
from ..models.user import UserCreate, UserInDB
from ..auth.jwt import get_password_hash
from motor.motor_asyncio import AsyncIOMotorDatabase

class UserService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.users

    async def create_user(self, user: UserCreate) -> UserInDB:
        """创建新用户"""
        # 检查用户名是否已存在
        if await self.collection.find_one({"username": user.username}):
            raise ValueError("Username already registered")
        
        # 检查邮箱是否已存在
        if await self.collection.find_one({"email": user.email}):
            raise ValueError("Email already registered")
        
        # 创建用户文档
        user_in_db = UserInDB(
            **user.dict(exclude={'password'}),
            hashed_password=get_password_hash(user.password)
        )
        
        # 插入数据库
        await self.collection.insert_one(user_in_db.dict())
        return user_in_db

    async def get_user(self, username: str) -> Optional[UserInDB]:
        """通过用户名获取用户"""
        user_dict = await self.collection.find_one({"username": username})
        if user_dict:
            return UserInDB(**user_dict)
        return None

    async def get_user_by_id(self, user_id: str) -> Optional[UserInDB]:
        """通过ID获取用户"""
        user_dict = await self.collection.find_one({"_id": ObjectId(user_id)})
        if user_dict:
            return UserInDB(**user_dict)
        return None

    async def update_user(self, user_id: str, update_data: dict) -> Optional[UserInDB]:
        """更新用户信息"""
        update_result = await self.collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": update_data}
        )
        if update_result.modified_count:
            return await self.get_user_by_id(user_id)
        return None
