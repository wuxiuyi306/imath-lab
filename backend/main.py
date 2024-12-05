from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import redis.asyncio as redis
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

app = FastAPI(title="iMathLab API")

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中需要设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB连接
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.imath_db

# Redis连接
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL)

@app.on_event("startup")
async def startup_db_client():
    try:
        # 验证MongoDB连接
        await mongo_client.admin.command('ping')
        # 验证Redis连接
        await redis_client.ping()
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_db_client():
    mongo_client.close()
    await redis_client.close()

@app.get("/")
async def root():
    return {"message": "Welcome to iMathLab API"}
