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
    predict_dates = find_predict_date(key)
    return dates, page, visit, key, predict_dates

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
    
def output_result(page, result, key, predict_dates):
    page_dates = key.index.values # the np.array of page_dates strings
    page_index = pd.Index(page)   # create panda.Index() from page array
    predic_dates_index = pd.Index(predict_dates) # create panda.Index() from predict_dates array
    n_out_page_dates = len(page_dates)
    with open('../results/submit_1.csv', mode = 'w', buffering = 131072) as out_f:
        print('Id,Visits', file = out_f)
        for i in range(n_out_page_dates):
            page_i = page_index.get_loc(page_dates[i][:-11])
            date_i = predic_dates_index.get_loc(page_dates[i][-10:])
            print(key.values[i][0], result[page_i][date_i], sep=',', file = out_f)
    return

def find_predict_date(key):
    '''
    Return list of dates that we need to predict their traffic
    '''
    page_dates = key.index.values
    # Assuming each page_dates item has the form 'pagename_YYYY-MM-DD'
    first_page_name = page_dates[0][:-11] # Remove the date from first page_dates entry
    predict_dates = np.array([x[-10:] for x in page_dates if first_page_name in x])
    return predict_dates

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


