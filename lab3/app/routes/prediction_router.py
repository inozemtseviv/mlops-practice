from fastapi import APIRouter
from app.models import PredictionRequest, PredictionResponse
from app.services.prediction_service import PredictionService


def get_router(ps: PredictionService):
    router = APIRouter()

    @router.post("/predict")
    def summarize(request: PredictionRequest) -> PredictionResponse:
        return PredictionResponse(result=ps.predict([
            request.sepalLength,
            request.sepalWidth,
            request.petalLength,
            request.sepalWidth,
        ]))

    return router
