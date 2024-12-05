from typing import Optional
import httpx
from ..core.config import get_settings
from ..models.user import WechatInfo

settings = get_settings()

class WechatService:
    @staticmethod
    async def get_session_info(code: str) -> Optional[dict]:
        """获取微信小程序会话信息"""
        url = "https://api.weixin.qq.com/sns/jscode2session"
        params = {
            "appid": settings.WECHAT_APP_ID,
            "secret": settings.WECHAT_APP_SECRET,
            "js_code": code,
            "grant_type": "authorization_code"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if "errcode" not in data or data["errcode"] == 0:
                    return data
            return None

    @staticmethod
    def create_wechat_info(session_info: dict, user_info: dict = None) -> WechatInfo:
        """创建微信用户信息"""
        return WechatInfo(
            openid=session_info["openid"],
            unionid=session_info.get("unionid"),
            nickname=user_info.get("nickName") if user_info else None,
            avatar_url=user_info.get("avatarUrl") if user_info else None
        )
