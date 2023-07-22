import xgboost as xgb
import joblib
import sklearn

import pandas as pd

X_train = pd.read_csv("../data/X_train.csv")
y_train = pd.read_csv("../data/y_train.csv")

X_test = pd.read_csv("../data/data.csv")

regressor=xgb.XGBRegressor(learning_rate = 0.01,
                           n_estimators  = 700,
                           max_depth     = 4,
                           eval_metric='rmse')

regressor.fit(X_train, y_train)

joblib.dump(regressor, "../models/xgbmodel.joblib")

print(regressor.predict(X_test))