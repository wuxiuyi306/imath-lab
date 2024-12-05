from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from bson import ObjectId

class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    disabled: bool = False
    
class WechatInfo(BaseModel):
    openid: str
    unionid: Optional[str] = None
    nickname: Optional[str] = None
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    password: Optional[str] = None
    wechat_info: Optional[WechatInfo] = None

class UserInDB(UserBase):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    hashed_password: Optional[str] = None
    wechat_info: Optional[WechatInfo] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_login: Optional[datetime] = None

    class Config:
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat()
        }

class User(UserBase):
    id: str
    wechat_info: Optional[WechatInfo] = None
    last_login: Optional[datetime] = None

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: str
    exp: Optional[datetime] = None
