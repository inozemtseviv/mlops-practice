import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

os.makedirs('lab1/data/train', exist_ok=True)
os.makedirs('lab1/data/test', exist_ok=True)


def get_mock_data(num_days):
    """
    Генерирует данные о температуре для указанного количества дней.
    Добавляет шум и аномалии.
    """
    # Базовая синусоида, имитирующая естественные колебания температур
    base_temperature = 10 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_days))
    
    # Добавление шума
    noise = 2.1 * np.random.randn(num_days)
    
    # Добавление аномалий
    anomaly_days = np.random.choice(range(num_days), size=int(0.05 * num_days), replace=False)
    base_temperature[anomaly_days] += np.random.randint(10, 20, size=len(anomaly_days))
    
    return base_temperature + noise


# Генерирую данные с 5 точек-датчиков температуры
point1 = get_mock_data(num_days=365*5)
point2 = get_mock_data(num_days=365*5)
point3 = get_mock_data(num_days=365*5)
point4 = get_mock_data(num_days=365*5)
point5 = get_mock_data(num_days=365*5)

# Создаю датафрейм со сгенерированными данными
df = pd.DataFrame({
    'point1': point1,
    'point2': point2,
    'point3': point3,
    'point4': point4,
    'point5': point5,
})

# Добавляю таргет - точку-датчик, которая находится в окружении прочих датчиков 
# и чудесным образом фиксирует среднее значение температуры
df['target'] = (df['point1'] + df['point2'] + df['point3'] + df['point4'] + df['point5']) / 5

# Разбиваю данные на тренировочные и тестовые
train, test = train_test_split(df, test_size=0.33, random_state=42)

# Сохраняю в файлы
train.to_csv('lab1/data/train/train.csv', index=False)
test.to_csv('lab1/data/test/test.csv', index=False)
