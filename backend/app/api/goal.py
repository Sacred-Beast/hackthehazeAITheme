from fastapi import APIRouter
from pydantic import BaseModel
from app.models.goal_extractor import GoalExtractor

router = APIRouter()
extractor = GoalExtractor()

class GoalInput(BaseModel):
    text: str

@router.post("/extract-goals")
def extract_goals(data: GoalInput):
    goals = extractor.extract_goals(data.text)
    return {"goals": goals}
