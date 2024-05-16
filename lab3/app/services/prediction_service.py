import pickle

from app.models import PredictionRequest


class PredictionService:
    def __init__(self, path_to_model):
        self.path_to_model = path_to_model

    def init(self):
        with open(f'{self.path_to_model}/model.pkl', 'rb') as file:
            self.model = pickle.load(file)

    def predict(self, data):
        return self.model.predict([data])
