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
    return dates, page, visit, key, predict_dates, readin

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
    
def output_result(page, result, key, predict_dates, output_filename = 'submit_1'):
    page_dates = key.index.values # the np.array of page_dates strings
    page_index = pd.Index(page)   # create panda.Index() from page array
    predic_dates_index = pd.Index(predict_dates) # create panda.Index() from predict_dates array
    n_out_page_dates = len(page_dates) # total number of output entry
    with open('../results/' + output_filename + '.csv', mode = 'w',
              buffering = 64*1024) as out_f:
        print('Id,Visits', file = out_f)
        for i in range(n_out_page_dates):
            page_i = page_index.get_loc(page_dates[i][:-11])
            date_i = predic_dates_index.get_loc(page_dates[i][-10:])
            print(key.values[i][0], result[page_i][date_i], sep=',',
                  file = out_f)
    return

def output_result2(page, result, key, predict_dates, output_filename = 'submit_1'):
    page_dates = key.index.values # the np.array of page_dates strings
    page_index = pd.Index(page)   # create panda.Index() from page array
    
    first_pred_date = np.datetime64(predict_dates[ 0])
    last_pred_date  = np.datetime64(predict_dates[-1])
    pred_period = last_pred_date - first_pred_date + np.timedelta64(1,'D')
    if pred_period != np.timedelta64(len(predict_dates), 'D'):
        print('!!! predict_dates not continuous !!!')
        # create panda.Index() from predict_dates array
        predic_dates_index = pd.Index(predict_dates) 
    else:
        predic_dates_index = pd.date_range(first_pred_date, 
                                           periods = pred_period, 
                                           freq = 'D', unit = 'D')
    result_df = pd.DataFrame(result, index = page_index, 
                             columns = predic_dates_index) # DataFrame of result
    n_out_page_dates = len(page_dates) # total number of output entry
    with open('../results/' + output_filename + '.csv', mode = 'w',
              buffering = 64*1024) as out_f:
        print('Id,Visits', file = out_f)
        for i in range(n_out_page_dates):
            print(key.values[i][0], 
                  result_df[page_dates[i][-10:]][page_dates[i][:-11]], 
                  sep=',', file = out_f)
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

def memory_usage(dates, page, visit, key, predict_dates, result = np.array([])):
    dates_kb = dates.nbytes // 1024
    page_kb = page.nbytes // 1024
    visit_kb = visit.nbytes // 1024
    key_kb = key.memory_usage(index = True, deep = True).sum() // 1024
    predict_dates_kb = predict_dates.nbytes // 1024
    result_kb = result.nbytes // 1024
    print(' dates:', dates_kb, ' page:', page_kb, ' visit:', visit_kb,
          ' key:', key_kb, ' predict_dates:', predict_dates_kb,
          ' result:', result_kb)
    sum_kb = dates_kb + page_kb + visit_kb + key_kb + predict_dates_kb + result_kb
    print('== total: ', sum_kb, '==')
    return sum_kb
    
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

    