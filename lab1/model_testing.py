import pickle
import pandas as pd
from sklearn.metrics import r2_score

# Загрузка модели
with open('lab1/model.pkl', 'rb') as file:
    model = pickle.load(file)

test_prep = pd.read_csv('lab1/data/test/test_prep.csv')
X = test_prep.drop('target', axis=1)
y = test_prep['target']

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

print(f'Метрика R2 на тестовой выборке: {r2}')