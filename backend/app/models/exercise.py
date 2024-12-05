from typing import Optional, List
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class ExerciseStep(BaseModel):
    """解题步骤"""
    description: str
    formula: Optional[str] = None

class ExerciseSolution(BaseModel):
    """题目解答"""
    steps: List[ExerciseStep]
    explanation: str

class ExerciseContent(BaseModel):
    """题目内容"""
    question: str
    options: Optional[List[str]] = None  # 选择题选项
    answer: str
    solution: ExerciseSolution

class ExerciseMetadata(BaseModel):
    """题目元数据"""
    difficulty: int = Field(ge=1, le=3)  # 难度等级1-3
    knowledge_points: List[str]  # 相关知识点ID
    time_estimate: int  # 预计完成时间（分钟）

class Exercise(BaseModel):
    """练习题目"""
    id: str = Field(default_factory=lambda: str(ObjectId()))
    type: str = Field(..., description="题目类型: choice(选择题), fill(填空题), calculation(计算题), proof(证明题)")
    content: ExerciseContent
    metadata: ExerciseMetadata
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat()
        }

class PhotoAnalysis(BaseModel):
    """拍照解答分析"""
    steps: List[dict] = Field(..., description="解答步骤分析，包含description(步骤描述)、isCorrect(是否正确)、suggestion(建议)")
    completeness: float = Field(..., ge=0, le=100, description="完整度百分比")
    overall_feedback: str

class ExerciseSubmission(BaseModel):
    """练习提交"""
    exercise_id: str
    user_answer: Optional[str] = None
    time_taken: Optional[int] = None  # 实际用时（秒）
    photo_submission: Optional[dict] = None  # 包含image_url和ai_analysis
    created_at: datetime = Field(default_factory=datetime.utcnow)

class PracticeSession(BaseModel):
    """练习会话"""
    id: str = Field(default_factory=lambda: str(ObjectId()))
    user_id: str
    exercises: List[ExerciseSubmission]
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None
    score: Optional[float] = None

    class Config:
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat()
        }
