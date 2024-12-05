from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from typing import Optional
import httpx
from ..models.user import User, UserCreate
from ..services.user_service import UserService
from ..auth.jwt import create_access_token, verify_token
import os
from ..auth.oauth2 import get_current_user

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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

@router.post("/login/wechat")
async def wechat_login(code: str):
    """
    微信登录接口
    """
    try:
        # 获取微信配置
        appid = os.getenv("WECHAT_APPID")
        secret = os.getenv("WECHAT_SECRET")
        
        # 请求微信API获取openid和session_key
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.weixin.qq.com/sns/jscode2session",
                params={
                    "appid": appid,
                    "secret": secret,
                    "js_code": code,
                    "grant_type": "authorization_code"
                }
            )
            wx_data = response.json()
            
        if "errcode" in wx_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"WeChat login failed: {wx_data['errmsg']}"
            )
            
        # 创建或更新用户
        openid = wx_data["openid"]
        # TODO: 实现用户创建/更新逻辑
        
        # 创建访问令牌
        access_token = create_access_token(data={"sub": openid})
        return {"access_token": access_token, "token_type": "bearer"}
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息
    """
    return current_user
