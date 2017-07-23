# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
def read_data():
    readin = pd.read_csv('../data/train_1.csv', index_col = 0)
    dates = readin.columns.values
    page = readin.index.values
    visit = readin.values
    
    key = pd.read_csv('../data/key_1.csv', index_col = 0)
    
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
    
def output_result(page, dates, result, key):
    return

def find_predict_date(key):
    page_dates = key.index.values
    first_page_name = '_'.join(page_dates[0].split('_')[:-1])
    return

#2129280
def read_test():
    return pd.read_csv('../data/key_1.csv')

#2128964
def read_test2():
    readin = pd.read_csv('../data/key_1.csv')
    return readin.values

#2128512
def read_test3():
    return pd.read_csv('../data/key_1.csv').values


