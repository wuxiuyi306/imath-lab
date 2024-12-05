from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

class Video(BaseModel):
    title: str
    url: str
    duration: str
    thumbnail: str

class Example(BaseModel):
    question: str
    solution: str
    explanation: str
    difficulty: int = Field(ge=1, le=3)

class Category(BaseModel):
    main: str
    sub: str

class Content(BaseModel):
    summary: str
    keyPoints: List[str]
    explanation: str
    examples: List[Example]
    commonMistakes: List[str]
    videos: List[Video]

class RelatedPoints(BaseModel):
    prerequisites: List[str]
    extensions: List[str]

class Metadata(BaseModel):
    difficulty: int = Field(ge=1, le=3)
    grade: int = Field(ge=7, le=9)  # 初中7-9年级
    term: int = Field(ge=1, le=2)
    chapter: int
    createTime: datetime = Field(default_factory=datetime.utcnow)
    updateTime: datetime = Field(default_factory=datetime.utcnow)

class KnowledgePointBase(BaseModel):
    title: str
    category: Category
    content: Content
    relatedPoints: RelatedPoints
    metadata: Metadata

class KnowledgePointCreate(KnowledgePointBase):
    pass

class KnowledgePointInDB(KnowledgePointBase):
    id: str = Field(default_factory=lambda: str(ObjectId()))

    class Config:
        json_encoders = {
            ObjectId: str
        }

class KnowledgePoint(KnowledgePointBase):
    id: str
