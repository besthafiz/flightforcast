
# import libraries
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# import the necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import subprocess
from IPython.display import display
# from sklearn.model_selection import KFold, StratifiedKFold#
import pandasql as ps
import mysql.connector

#create example of linear regression

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([2,4,6,8,10,12,14,16,18,20])

# create a linear regression model
model = LinearRegression()
model.fit(x.reshape(-1,1), y)

# make a prediction
yhat = model.predict([[11], [12]])
print('Predicted: %.3f' % yhat[0])
print('Predicted: %.3f' % yhat[1])

# plot the data and the model prediction
plt.scatter(x, y)
line = np.arange(1, 12).reshape(-1, 1)
plt.plot(line, model.predict(line), color='red')
plt.show()


