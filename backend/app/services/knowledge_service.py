from typing import List, Optional
from bson import ObjectId
from ..models.knowledge import KnowledgePointCreate, KnowledgePointInDB, KnowledgePoint
from motor.motor_asyncio import AsyncIOMotorDatabase

class KnowledgeService:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db.knowledge_points

    async def create_knowledge_point(self, knowledge_point: KnowledgePointCreate) -> KnowledgePointInDB:
        """创建新知识点"""
        knowledge_point_db = KnowledgePointInDB(**knowledge_point.dict())
        await self.collection.insert_one(knowledge_point_db.dict())
        return knowledge_point_db

    async def get_knowledge_point(self, knowledge_id: str) -> Optional[KnowledgePointInDB]:
        """通过ID获取知识点"""
        knowledge_dict = await self.collection.find_one({"id": knowledge_id})
        if knowledge_dict:
            return KnowledgePointInDB(**knowledge_dict)
        return None

    async def list_knowledge_points(
        self,
        grade: Optional[int] = None,
        term: Optional[int] = None,
        chapter: Optional[int] = None,
        difficulty: Optional[int] = None,
        skip: int = 0,
        limit: int = 10
    ) -> List[KnowledgePointInDB]:
        """获取知识点列表，支持分页和筛选"""
        filter_query = {}
        if grade:
            filter_query["metadata.grade"] = grade
        if term:
            filter_query["metadata.term"] = term
        if chapter:
            filter_query["metadata.chapter"] = chapter
        if difficulty:
            filter_query["metadata.difficulty"] = difficulty

        cursor = self.collection.find(filter_query)
        cursor.skip(skip).limit(limit)
        knowledge_points = await cursor.to_list(length=limit)
        return [KnowledgePointInDB(**kp) for kp in knowledge_points]

    async def update_knowledge_point(
        self,
        knowledge_id: str,
        knowledge_point: KnowledgePointCreate
    ) -> Optional[KnowledgePointInDB]:
        """更新知识点"""
        update_result = await self.collection.update_one(
            {"id": knowledge_id},
            {"$set": knowledge_point.dict()}
        )
        if update_result.modified_count:
            return await self.get_knowledge_point(knowledge_id)
        return None

    async def delete_knowledge_point(self, knowledge_id: str) -> bool:
        """删除知识点"""
        delete_result = await self.collection.delete_one({"id": knowledge_id})
        return delete_result.deleted_count > 0

    async def get_related_points(self, knowledge_id: str) -> dict:
        """获取相关知识点"""
        knowledge_point = await self.get_knowledge_point(knowledge_id)
        if not knowledge_point:
            return {"prerequisites": [], "extensions": []}

        # 获取前置知识点
        prerequisites = []
        for pre_id in knowledge_point.relatedPoints.prerequisites:
            pre_point = await self.get_knowledge_point(pre_id)
            if pre_point:
                prerequisites.append(pre_point)

        # 获取扩展知识点
        extensions = []
        for ext_id in knowledge_point.relatedPoints.extensions:
            ext_point = await self.get_knowledge_point(ext_id)
            if ext_point:
                extensions.append(ext_point)

        return {
            "prerequisites": prerequisites,
            "extensions": extensions
        }
