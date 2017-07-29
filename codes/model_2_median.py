# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:36:00 2017

@author: Louis
"""
print('')
print('Kaggle - Web Traffic Time Series Forecasting')
print('         by Sky Huang and Louis Yang')
model_name = 'model_02_median'
print('Model 02 - Median')

import numpy as np
import data_processing as dp
print('%%% Reading data...', end = '', flush = True)
dates, page, visit, key, predict_dates, readin = dp.read_data()
print('done!')

number_days = len(visit[0])
number_pages = len(page)
"""
print('%%%%% Overview of the data: %%%%%')
print('  Number of pages:', number_pages)
print('  Number of days of data:', number_days)
print('  visit[0]:', visit[0])
print('  page[:5]', page[:5])
print('  Plot a few data:')
dp.plot_some_visit(visit, page)
"""
number_predict_days = len(predict_dates)
visit_median = np.around(np.nan_to_num(np.nanmedian(visit, axis = 1))).astype(int)

result = np.repeat(np.array([visit_median]).transpose(), number_predict_days, 
                   axis = 1)

print('%%% Writing result...', end = '')
dp.output_result(page, result, key, predict_dates, 'submit_1_' + model_name)
print('done!')
