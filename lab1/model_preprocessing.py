import pandas as pd
from sklearn.preprocessing import StandardScaler

train = pd.read_csv('lab1/data/train/train.csv')
test = pd.read_csv('lab1/data/test/test.csv')

scaler = StandardScaler()
scaler.fit(train)

train_prep = pd.DataFrame(scaler.transform(train), index=train.index, columns=train.columns)
train_prep['target'] = train['target']

test_prep = pd.DataFrame(scaler.transform(test), index=test.index, columns=test.columns)
test_prep['target'] = test['target']

train_prep.to_csv('lab1/data/train/train_prep.csv', index=False)
test_prep.to_csv('lab1/data/test/test_prep.csv', index=False)
