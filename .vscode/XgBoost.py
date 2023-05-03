# create exmple of xgboost model    
import xgboost as xgb
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pytest

# create math class functions
# load data
boston = load_boston()

# split data into train and test sets
X, y = boston.data, boston.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# instantiate xgboost regressor
xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 10)

# fit the regressor to the training set
xg_reg.fit(X_train, y_train)

# make predictions for the test set
preds = xg_reg.predict(X_test)

# calculate the rmse
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE: %f" % (rmse))

# create a DMatrix for the training set
data_dmatrix = xgb.DMatrix(data=X, label=y)

# create the parameter dictionary
params = {"objective":"reg:squarederror",'colsample_bytree': 0.3,'learning_rate': 0.1,
                'max_depth': 5, 'alpha': 10}

# instantiate the regressor
                    


