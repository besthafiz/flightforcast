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

# craete dynamic function to load the data for any file
def load_data_dynamic(fileName):
    dir=os.path.dirname(os.path.abspath("__file__"))
    #dir = os.path.dirname(__file__)
    filename = dir+'\\data\\' + fileName;
    return pd.read_csv(filename, low_memory=False,encoding='latin-1')  

# call load_data_dynamic function to load the data
df = load_data_dynamic('selectedFlightData.csv')
#display(df.head(5))















