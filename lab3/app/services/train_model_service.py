import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle


class TrainModelService:
    def __init__(self, path_to_model):
        self.path_to_model = path_to_model

    def train(self):
        RANDOM_STATE = 42

        iris = load_iris()
        X = iris['data']
        y = iris['target']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, random_state=RANDOM_STATE, stratify=y)

        model = DecisionTreeClassifier(
            random_state=RANDOM_STATE, max_depth=5, max_features=5)
        model.fit(X_train, y_train)

        pred = model.predict(X_test)
        print(f'Метрика Accuracy на тестовой выборке: {accuracy_score(y_test, pred,):.2f}')

        os.makedirs(self.path_to_model, exist_ok=True)

        with open(f'{self.path_to_model}/model.pkl', 'wb') as file:
            pickle.dump(model, file)
