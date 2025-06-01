from fastapi import APIRouter
from pydantic import BaseModel
from app.models.skill_gap_analyzer import SkillGapAnalyzer

router = APIRouter()
analyzer = SkillGapAnalyzer()

class SkillGapInput(BaseModel):
    career_path: str
    user_skills: list[str]

@router.post("/analyze-skill-gap")
def analyze_gap(data: SkillGapInput):
    gap = analyzer.analyze(data.career_path, data.user_skills)
    return {"missing_skills": gap}
