# create linear regression model exmple class 
# import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

# load the diabetes dataset
diabetes = datasets.load_diabetes()

# use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# create linear regression object
regr = linear_model.LinearRegression()

# train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# the coefficients
print('Coefficients: ', regr.coef_)
# the mean squared error
print("Mean squared error: %.2f" % np.mean((diabetes_y_pred - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())
plt.show()
