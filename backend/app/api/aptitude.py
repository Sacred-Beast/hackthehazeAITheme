from fastapi import APIRouter, HTTPException
from app.models.aptitude_model import AptitudeModel

router = APIRouter()
model = AptitudeModel()

@router.post("/predict-aptitude")
def predict_aptitude(scores: list[float]):
    if len(scores) != 3:
        raise HTTPException(status_code=400, detail="Please provide exactly three scores.")
    result = model.predict(scores)
    return {"aptitude_class": result}
