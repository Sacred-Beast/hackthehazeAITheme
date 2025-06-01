from fastapi import APIRouter
from pydantic import BaseModel
from app.models.career_recommender import CareerRecommender

router = APIRouter()
recommender = CareerRecommender()

class AptitudeInput(BaseModel):
    aptitude_class: int

@router.post("/recommend-careers")
def recommend_careers(data: AptitudeInput):
    careers = recommender.recommend(data.aptitude_class)
    return {"careers": careers}
