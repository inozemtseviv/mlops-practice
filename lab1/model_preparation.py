import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

train_prep = pd.read_csv('lab1/data/train/train_prep.csv')
X = train_prep.drop('target', axis=1)
y = train_prep['target']

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)
r2 = r2_score(y, y_pred)

# Сохранение модели с помощью pickle
with open('lab1/model.pkl', 'wb') as file:
    pickle.dump(model, file)
