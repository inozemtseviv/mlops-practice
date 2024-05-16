from pydantic import BaseModel


class PredictionRequest(BaseModel):
    sepalLength: float
    sepalWidth: float
    petalLength: float
    petalWidth: float

class PredictionResponse(BaseModel):
    result: int