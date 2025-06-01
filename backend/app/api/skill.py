from fastapi import APIRouter
from pydantic import BaseModel
from app.models.skill_mapper import SkillMapper

router = APIRouter()
mapper = SkillMapper()

class SkillsInput(BaseModel):
    skills: list[str]

@router.post("/map-skills")
def map_skills(data: SkillsInput):
    recommendations = mapper.map_skills(data.skills)
    return {"recommendations": recommendations}
