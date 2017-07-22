# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
def read_data():
    readin = pd.read_csv('../data/train_1.csv')
    dates = readin.columns.values[1:]
    page = readin.iloc[:,0].values
    visit = readin.iloc[:,1:].values
    
    key = pd.read_csv('../data/key_1.csv').values
    
    return dates, page, visit, key

# Plot the ith visit data
def plot_visit(i, visit, page):
    if i < len(page):
        print('Visit data[',i,']: ',page[i])
        plt.plot(visit[i])
        plt.show()
    else:
        print('Out of range')

# Show some data
def plot_some_visit(visit, page, yscale = 'linear'):
    n = len(page)
    plot_total = 8
    plot_i = np.random.randint(0, n, size = plot_total)
    print('Plot visit for', plot_i)
    plt.figure(1, figsize = (12, 5))
    for i in range(plot_total):
        plt.subplot(2, 4, i + 1)
        plt.yscale(yscale)
        plt.title(plot_i[i])
        plt.grid(True)
        plt.plot(visit[plot_i[i]])
    plt.tight_layout()
    plt.show()