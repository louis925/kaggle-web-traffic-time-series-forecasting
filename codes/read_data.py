# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
read_data():
    readin = pd.read_csv('../data/train_1.csv')
    page= readin.iloc[:,0].values
    visit= readin.iloc[:,1:].values

    return page, visit
