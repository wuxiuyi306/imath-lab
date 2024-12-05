from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from ..core.database import db
from ..models.exercise import Exercise, PracticeSession, ExerciseSubmission

class ExerciseService:
    def __init__(self):
        self.db = db.get_db()
        self.exercises_collection = self.db["exercises"]
        self.sessions_collection = self.db["practice_sessions"]
    
    async def create_exercise(self, exercise: Exercise) -> Exercise:
        """创建新的练习题"""
        exercise_dict = exercise.dict()
        result = await self.exercises_collection.insert_one(exercise_dict)
        exercise_dict["id"] = str(result.inserted_id)
        return Exercise(**exercise_dict)
    
    async def get_exercise(self, exercise_id: str) -> Optional[Exercise]:
        """获取练习题详情"""
        exercise = await self.exercises_collection.find_one({"_id": ObjectId(exercise_id)})
        if exercise:
            exercise["id"] = str(exercise["_id"])
            return Exercise(**exercise)
        return None
    
    async def get_exercises_by_knowledge(self, knowledge_id: str, difficulty: Optional[int] = None) -> List[Exercise]:
        """获取指定知识点的练习题"""
        query = {"metadata.knowledge_points": knowledge_id}
        if difficulty:
            query["metadata.difficulty"] = difficulty
        
        exercises = []
        cursor = self.exercises_collection.find(query)
        async for exercise in cursor:
            exercise["id"] = str(exercise["_id"])
            exercises.append(Exercise(**exercise))
        return exercises
    
    async def create_practice_session(self, user_id: str, exercise_ids: List[str]) -> PracticeSession:
        """创建练习会话"""
        session = PracticeSession(
            user_id=user_id,
            exercises=[
                ExerciseSubmission(exercise_id=exercise_id)
                for exercise_id in exercise_ids
            ]
        )
        session_dict = session.dict()
        result = await self.sessions_collection.insert_one(session_dict)
        session_dict["id"] = str(result.inserted_id)
        return PracticeSession(**session_dict)
    
    async def submit_exercise(
        self,
        session_id: str,
        exercise_id: str,
        user_answer: Optional[str] = None,
        time_taken: Optional[int] = None,
        photo_submission: Optional[dict] = None
    ) -> bool:
        """提交练习答案"""
        update_data = {
            "user_answer": user_answer,
            "time_taken": time_taken,
            "photo_submission": photo_submission,
            "created_at": datetime.utcnow()
        }
        
        result = await self.sessions_collection.update_one(
            {
                "_id": ObjectId(session_id),
                "exercises.exercise_id": exercise_id
            },
            {
                "$set": {
                    "exercises.$": update_data
                }
            }
        )
        return result.modified_count > 0
    
    async def complete_session(self, session_id: str, score: float) -> bool:
        """完成练习会话"""
        result = await self.sessions_collection.update_one(
            {"_id": ObjectId(session_id)},
            {
                "$set": {
                    "end_time": datetime.utcnow(),
                    "score": score
                }
            }
        )
        return result.modified_count > 0
    
    async def get_user_sessions(self, user_id: str, limit: int = 10) -> List[PracticeSession]:
        """获取用户的练习记录"""
        sessions = []
        cursor = self.sessions_collection.find(
            {"user_id": user_id}
        ).sort("start_time", -1).limit(limit)
        
        async for session in cursor:
            session["id"] = str(session["_id"])
            sessions.append(PracticeSession(**session))
        return sessions
