from fastapi import APIRouter, Depends, HTTPException
from app.models import Prediction, PredictionCreate
from app.database import get_db

router = APIRouter()

@router.get("/", response_model=list[Prediction])
async def get_predictions(post_id: str = None, db=Depends(get_db)):
    query = db.table("predictions").select("*")
    if post_id:
        query = query.eq("post_id", post_id)
    result = query.execute()
    return result.data

@router.post("/", response_model=Prediction)
async def create_prediction(prediction: PredictionCreate, db=Depends(get_db)):
    result = db.table("predictions").insert(prediction.model_dump()).execute()
    return result.data[0]

@router.post("/{prediction_id}/resolve")
async def resolve_prediction(prediction_id: str, is_correct: bool, db=Depends(get_db)):
    result = db.table("predictions").update({
        "is_resolved": True,
        "is_correct": is_correct
    }).eq("id", prediction_id).execute()
    return result.data[0]
