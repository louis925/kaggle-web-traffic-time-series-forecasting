# Importing libraries
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
def read_data():
    readin = pd.read_csv('../data/train_1.csv')
    dates = readin.columns.values[1:]
    page = readin.iloc[:,0].values
    visit = readin.iloc[:,1:].values
    
    key = pd.read_csv('../data/key_1.csv').values
    
    return dates, page, visit, key
