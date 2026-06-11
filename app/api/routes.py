from fastapi import APIRouter
from app.schemas.prediction_schema import (
    QuestionPair,
    PredictionResponse
)
from app.services.prediction_service import predict_duplicate

router = APIRouter()

@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(data: QuestionPair):

    pred, prob = predict_duplicate(
        data.question1,
        data.question2
    )

    label = "Duplicate" if pred == 1 else "Not Duplicate"

    return {
        "prediction": label,
        "confidence": round(float(prob), 4)
    }