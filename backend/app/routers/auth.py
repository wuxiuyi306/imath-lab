from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from typing import Optional
import httpx
from ..models.user import User, UserCreate, Token
from ..services.user_service import UserService
from ..services.auth_service import AuthService
from ..auth.jwt import create_access_token, verify_token
import os
from ..auth.oauth2 import get_current_user
from ..core.config import get_settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
settings = get_settings()

@router.post("/register", response_model=User)
async def register(user: UserCreate, user_service: UserService = Depends()):
    """
    用户注册
    """
    try:
        user_db = await user_service.create_user(user)
        return User(**user_db.dict())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends()):
    """
    用户登录
    """
    user = await user_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """获取当前用户"""
    token_data = await AuthService.verify_token(token)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="无效的认证凭据",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 从数据库获取用户
    user_doc = await db.get_db()["users"].find_one({"_id": ObjectId(token_data.user_id)})
    if not user_doc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return User(**user_doc)

@router.post("/login/wechat", response_model=Token)
async def wechat_login(code: str, user_info: Optional[dict] = None):
    """微信登录"""
    result = await AuthService.authenticate_wechat(code, user_info)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="微信登录失败",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user, access_token = result
    return Token(access_token=access_token)

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """获取当前用户信息"""
    return current_user
