from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from ..models.exercise import Exercise, PracticeSession, ExerciseSubmission
from ..models.user import User
from ..services.exercise_service import ExerciseService
from .auth import get_current_user

router = APIRouter()

@router.post("/exercises", response_model=Exercise)
async def create_exercise(
    exercise: Exercise,
    current_user: User = Depends(get_current_user),
    exercise_service: ExerciseService = Depends()
):
    """创建新的练习题"""
    return await exercise_service.create_exercise(exercise)

@router.get("/exercises/{exercise_id}", response_model=Exercise)
async def get_exercise(
    exercise_id: str,
    exercise_service: ExerciseService = Depends()
):
    """获取练习题详情"""
    exercise = await exercise_service.get_exercise(exercise_id)
    if not exercise:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="练习题不存在"
        )
    return exercise

@router.get("/knowledge/{knowledge_id}/exercises", response_model=List[Exercise])
async def get_exercises_by_knowledge(
    knowledge_id: str,
    difficulty: Optional[int] = None,
    exercise_service: ExerciseService = Depends()
):
    """获取知识点相关的练习题"""
    return await exercise_service.get_exercises_by_knowledge(knowledge_id, difficulty)

@router.post("/practice", response_model=PracticeSession)
async def start_practice(
    exercise_ids: List[str],
    current_user: User = Depends(get_current_user),
    exercise_service: ExerciseService = Depends()
):
    """开始练习"""
    return await exercise_service.create_practice_session(current_user.id, exercise_ids)

@router.post("/practice/{session_id}/submit/{exercise_id}")
async def submit_exercise(
    session_id: str,
    exercise_id: str,
    submission: ExerciseSubmission,
    current_user: User = Depends(get_current_user),
    exercise_service: ExerciseService = Depends()
):
    """提交练习答案"""
    success = await exercise_service.submit_exercise(
        session_id,
        exercise_id,
        submission.user_answer,
        submission.time_taken,
        submission.photo_submission
    )
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="提交答案失败"
        )
    return {"message": "提交成功"}

@router.post("/practice/{session_id}/complete")
async def complete_practice(
    session_id: str,
    score: float,
    current_user: User = Depends(get_current_user),
    exercise_service: ExerciseService = Depends()
):
    """完成练习"""
    success = await exercise_service.complete_session(session_id, score)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="完成练习失败"
        )
    return {"message": "练习已完成"}

@router.get("/practice/history", response_model=List[PracticeSession])
async def get_practice_history(
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    exercise_service: ExerciseService = Depends()
):
    """获取练习历史"""
    return await exercise_service.get_user_sessions(current_user.id, limit)
