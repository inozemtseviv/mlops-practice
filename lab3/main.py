import os
from fastapi import FastAPI
from dotenv import load_dotenv

from app.routes.prediction_router import get_router
from app.services.train_model_service import TrainModelService
from app.services.prediction_service import PredictionService

load_dotenv()

path_to_model = os.getenv("PATH_TO_MODEL", "")

tms = TrainModelService(path_to_model)
tms.train()

ps = PredictionService(path_to_model)
ps.init()

app = FastAPI()
app.include_router(get_router(ps))
