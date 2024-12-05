from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import redis.asyncio as redis
from dotenv import load_dotenv

from app.core.config import get_settings
from app.core.database import db
from app.routers import auth, knowledge

# 加载环境变量
load_dotenv()
settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中需要设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis连接
redis_client = redis.from_url(settings.REDIS_URL)

@app.on_event("startup")
async def startup_db_client():
    try:
        # 连接数据库
        await db.connect()
        # 验证Redis连接
        await redis_client.ping()
        print("Successfully connected to database")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_db_client():
    await db.disconnect()
    await redis_client.close()

# 注册路由
app.include_router(auth.router, prefix=f"{settings.API_V1_STR}/auth", tags=["认证"])
app.include_router(knowledge.router, prefix=f"{settings.API_V1_STR}/knowledge", tags=["知识点"])

@app.get("/")
async def root():
    return {
        "name": settings.PROJECT_NAME,
        "version": "1.0.0",
        "description": "智能数学学习平台API"
    }
