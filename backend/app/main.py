from fastapi import FastAPI, Query
from typing import List

from app.core.config import settings
from app.core.logging_config import logger
from app.services.aptitude_service import AptitudeService
from app.services.goal_service import GoalService
from app.services.skill_service import SkillService
from app.services.recommendation_service import RecommendationService
from app.services.skillgap_service import SkillGapService
from app.core.constants import APTITUDE_LEVELS

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION
)

# Instantiate services
aptitude_service = AptitudeService()
goal_service = GoalService()
skill_service = SkillService()
recommendation_service = RecommendationService()
skillgap_service = SkillGapService()

@app.get("/")
def root():
    return {"message": "Career Guidance Engine API is running 🚀"}

@app.post("/predict-aptitude/")
def predict_aptitude(scores: List[float]):
    aptitude_class = aptitude_service.predict_aptitude(scores)
    level = APTITUDE_LEVELS.get(aptitude_class, "Unknown")
    logger.info(f"Aptitude scores: {scores} => Level: {level}")
    return {"aptitude_level": level, "class": aptitude_class}

@app.post("/extract-goals/")
def extract_goals(text: str = Query(...)):
    goals = goal_service.extract_goals(text)
    logger.info(f"Extracted goals from text: {goals}")
    return {"goals": goals}

@app.post("/map-skills/")
def map_skills(skills: List[str]):
    careers = skill_service.map_skills(skills)
    logger.info(f"Mapped skills {skills} to careers {careers}")
    return {"recommended_careers": careers}

@app.get("/recommend-careers/")
def recommend(aptitude_class: int):
    careers = recommendation_service.recommend_careers(aptitude_class)
    logger.info(f"Career recommendations for aptitude class {aptitude_class}: {careers}")
    return {"recommended_careers": careers}

@app.post("/skill-gap/")
def skill_gap(career_path: str, user_skills: List[str]):
    missing_skills = skillgap_service.analyze_gap(career_path, user_skills)
    logger.info(f"Missing skills for {career_path}: {missing_skills}")
    return {"career_path": career_path, "missing_skills": missing_skills}
