from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from ..core.config import get_settings
from ..models.user import TokenData, User, UserInDB
from ..core.database import db
from .wechat_service import WechatService

settings = get_settings()

class AuthService:
    @staticmethod
    def create_access_token(user_id: str) -> str:
        """创建访问令牌"""
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode = {"user_id": str(user_id), "exp": expire}
        return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    @staticmethod
    async def verify_token(token: str) -> Optional[TokenData]:
        """验证令牌"""
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
            user_id = payload.get("user_id")
            if user_id is None:
                return None
            return TokenData(user_id=user_id, exp=payload.get("exp"))
        except JWTError:
            return None

    @staticmethod
    async def authenticate_wechat(code: str, user_info: dict = None) -> Optional[tuple[User, str]]:
        """微信登录认证"""
        wechat_service = WechatService()
        session_info = await wechat_service.get_session_info(code)
        
        if not session_info:
            return None
            
        # 查找或创建用户
        users_collection = db.get_db()["users"]
        user_doc = await users_collection.find_one({"wechat_info.openid": session_info["openid"]})
        
        if user_doc:
            # 更新用户信息
            user_doc["last_login"] = datetime.utcnow()
            if user_info:
                user_doc["wechat_info"]["nickname"] = user_info.get("nickName")
                user_doc["wechat_info"]["avatar_url"] = user_info.get("avatarUrl")
            await users_collection.update_one(
                {"_id": user_doc["_id"]},
                {"$set": {
                    "last_login": user_doc["last_login"],
                    "wechat_info": user_doc["wechat_info"]
                }}
            )
        else:
            # 创建新用户
            wechat_info = wechat_service.create_wechat_info(session_info, user_info)
            user_doc = UserInDB(
                username=f"wx_{session_info['openid'][:8]}",
                wechat_info=wechat_info
            ).dict()
            await users_collection.insert_one(user_doc)
        
        # 创建访问令牌
        access_token = AuthService.create_access_token(str(user_doc["_id"]))
        user = User(**user_doc)
        
        return user, access_token
