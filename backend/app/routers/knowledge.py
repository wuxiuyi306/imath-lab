from fastapi import APIRouter, HTTPException, Depends, Query
from typing import List, Optional
from ..models.knowledge import (
    KnowledgePoint,
    KnowledgePointCreate,
    KnowledgePointInDB
)
from ..services.knowledge_service import KnowledgeService
from ..auth.oauth2 import get_current_active_user

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

@router.post("/", response_model=KnowledgePoint)
async def create_knowledge_point(
    knowledge_point: KnowledgePointCreate,
    knowledge_service: KnowledgeService = Depends(),
    current_user: dict = Depends(get_current_active_user)
):
    """
    创建新知识点
    """
    try:
        return await knowledge_service.create_knowledge_point(knowledge_point)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{knowledge_id}", response_model=KnowledgePoint)
async def get_knowledge_point(
    knowledge_id: str,
    knowledge_service: KnowledgeService = Depends()
):
    """
    获取知识点详情
    """
    knowledge_point = await knowledge_service.get_knowledge_point(knowledge_id)
    if not knowledge_point:
        raise HTTPException(status_code=404, detail="Knowledge point not found")
    return knowledge_point

@router.get("/", response_model=List[KnowledgePoint])
async def list_knowledge_points(
    grade: Optional[int] = Query(None, ge=7, le=9),
    term: Optional[int] = Query(None, ge=1, le=2),
    chapter: Optional[int] = Query(None),
    difficulty: Optional[int] = Query(None, ge=1, le=3),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    knowledge_service: KnowledgeService = Depends()
):
    """
    获取知识点列表，支持分页和筛选
    """
    return await knowledge_service.list_knowledge_points(
        grade=grade,
        term=term,
        chapter=chapter,
        difficulty=difficulty,
        skip=skip,
        limit=limit
    )

@router.put("/{knowledge_id}", response_model=KnowledgePoint)
async def update_knowledge_point(
    knowledge_id: str,
    knowledge_point: KnowledgePointCreate,
    knowledge_service: KnowledgeService = Depends(),
    current_user: dict = Depends(get_current_active_user)
):
    """
    更新知识点
    """
    updated_point = await knowledge_service.update_knowledge_point(
        knowledge_id,
        knowledge_point
    )
    if not updated_point:
        raise HTTPException(status_code=404, detail="Knowledge point not found")
    return updated_point

@router.delete("/{knowledge_id}")
async def delete_knowledge_point(
    knowledge_id: str,
    knowledge_service: KnowledgeService = Depends(),
    current_user: dict = Depends(get_current_active_user)
):
    """
    删除知识点
    """
    success = await knowledge_service.delete_knowledge_point(knowledge_id)
    if not success:
        raise HTTPException(status_code=404, detail="Knowledge point not found")
    return {"message": "Knowledge point deleted successfully"}

@router.get("/{knowledge_id}/related", response_model=dict)
async def get_related_points(
    knowledge_id: str,
    knowledge_service: KnowledgeService = Depends()
):
    """
    获取相关知识点（前置和扩展）
    """
    knowledge_point = await knowledge_service.get_knowledge_point(knowledge_id)
    if not knowledge_point:
        raise HTTPException(status_code=404, detail="Knowledge point not found")
    return await knowledge_service.get_related_points(knowledge_id)
