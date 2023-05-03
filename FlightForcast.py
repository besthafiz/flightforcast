import csv
from matplotlib import pyplot
import numpy as np
import pandas as pd
from pandas import set_option

headernames = ['col1','col2','col3','col4','type']
path = r"..\data\iris.csv"
data = pd.read_csv(path, names=headernames)
set_option('display.width', 100)
set_option('precision', 2)
print(data)
print(data.shape)
print(data.dtypes)
print(data.describe())
count_class = data.groupby('type').size()
print(count_class)
correlations = data.corr(method='pearson')
print(correlations)
print(data.skew())
#Univariate Plots: Understanding Attributes Independently - start

#Histograms
#data.hist()

#Density Plots
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

#Box and Whisker Plots
#data.plot(kind='box', subplots=True, layout=(3,3), sharex=False,sharey=False)
#Univariate Plots: Understanding Attributes Independently - end


#Multivariate Plots: Interaction Among Multiple Variables
# Correlation Matrix Plot
# fig = pyplot.figure()
# ax = fig.add_subplot(111)
# cax = ax.matshow(correlations, vmin=-1, vmax=1)
# fig.colorbar(cax)
# ticks = np.arange(0,5,1)
# ax.set_xticks(ticks)
# ax.set_yticks(ticks)
# ax.set_xticklabels(headernames)
# ax.set_yticklabels(headernames)
#Correlation Matrix Plot

#Scatter Matrix Plot
#scatter_matrix(data)
#pd.plotting.scatter_matrix(data)


pyplot.show()








# df = pandas.read_csv(path, 
#             index_col='col1', 
#             parse_dates=['col5'], 
#             header=0, 
#             names=headernames)

# with open(path,'r') as f:
#    reader = csv.reader(f,delimiter = ',')
#    headers = next(reader)
#    print(headers)
#    data = list(reader)
# #    data = np.array(data).astype(object)
#    print(data[0])

# d = {'x': [1, 2, 3], 'y': np.array([20, 40, 80]), 'z': 100}
# df1=pd.DataFrame(d)
# print(df1)
# print(dir(np))   