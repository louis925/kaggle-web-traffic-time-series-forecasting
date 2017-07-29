# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:55:00 2017

@author: Louis
"""
print('')
print('Kaggle - Web Traffic Time Series Forecasting')
print('         by Sky Huang and Louis Yang')
model_name = 'model_03_weekday'
print('Model 03 - Weekday')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import data_processing as dp
import datetime # For timing

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
# Note dates[0] count as day = 0
# weekday: Monday = 0; Sunday = 6
first_weekday = pd.to_datetime(dates[0]).weekday()
def day_to_weekday(day):
    return first_weekday + day % 7
# Note predict_dates[0] count as predict_day = 0
first_predict_weekday = pd.to_datetime(predict_dates[0]).weekday()
def predict_day_to_weekday(predict_day):
    return first_predict_weekday + predict_day % 7
# np.nanmean(visit[0])

# Submodel 1 - Mean
print('Computing the mean in each weekday...')
weekday_visit_mean = [[np.nanmean(visit_p[d::7]) for d in range(7)] \
                       for visit_p in visit] # Takes 69 sec to run
weekday_visit_mean = np.nan_to_num(weekday_visit_mean)
weekday_visit_mean_align = np.roll(weekday_visit_mean, first_weekday, 
                                   axis = 1)
weekday_pred_visit_mean = np.roll(weekday_visit_mean_align, 
                                  -first_predict_weekday, axis = 1)
result_mean = np.tile(weekday_pred_visit_mean, number_predict_days // 7 + 1)

# Submodel 2 - Median
print('Computing the median in each weekday...')
weekday_visit_median = [[np.nanmedian(visit_p[d::7]) for d in range(7)] \
                         for visit_p in visit] # Takes ~min to run
weekday_visit_median = np.nan_to_num(weekday_visit_median)
weekday_visit_median_align = np.roll(weekday_visit_median, first_weekday, 
                                     axis = 1)
weekday_pred_visit_median = np.roll(weekday_visit_median_align, 
                                    -first_predict_weekday, axis = 1)
result_median = np.tile(weekday_pred_visit_median, number_predict_days // 7 + 1)

print('%%% Writing result for submodel 1 - Mean')#, end = '', flush = True)
ini_time = datetime.datetime.now()
print('%%% Start  at', ini_time)
dp.output_result(page, result_mean, key, predict_dates, 
                 'submit_1_' + model_name + '_1_mean')
fin_time = datetime.datetime.now()
print('%%% Finish at', fin_time)
print('%%% Time spent:', fin_time - ini_time)

print('%%% Writing result for submodel 2 - Median')#, end = '', flush = True)
ini_time = datetime.datetime.now()
print('%%% Start  at', ini_time)
dp.output_result(page, result_median, key, predict_dates, 
                 'submit_1_' + model_name + '_2_median')
fin_time = datetime.datetime.now()
print('%%% Finish at', fin_time)
print('%%% Time spent:', fin_time - ini_time)

"""
# Check result
i_check = 500
plt.plot(visit[i_check][7:14])
plt.plot(weekday_visit_mean[i_check])
plt.show()
plt.plot(weekday_visit_mean[i_check])
plt.plot(weekday_visit_mean_align[i_check])
plt.show()
"""

"""
# for testing
weekday_visit_small = [[np.nanmean(visit_p[d::7]) for d in range(7)] \
                  for visit_p in visit[:1000]]
weekday_visit_small = np.nan_to_num(weekday_visit_small)
weekday_visit_small 
first_weekday # for the run 1 data, first_weekday(2015/7/1) = 2
weekday_visit_dummy = np.array([(np.array(list(range(7))) + first_weekday) % 7] * 3)
weekday_visit_dummy # should be [first_weekday, first_weekday + 1, ...]
np.roll(weekday_visit_dummy, first_weekday, axis = 1) # should be [[0,1,2,...,6],...
np.roll(weekday_visit_small, first_weekday, axis = 1)
weekday_visit_small
"""

"""
# for testing 2
# First apply it to a dummy data which = weekday and is aligned
weekday_visit_a_dummy = np.array([np.array(list(range(7)))] * 3)
weekday_visit_a_dummy
# Shift so that the first column corresponds to first_predict_weekday (Ex: = 6)
weekday_pred_visit_dummy = np.roll(weekday_visit_a_dummy, 
                                   -first_predict_weekday, axis = 1)
weekday_pred_visit_dummy 
first_predict_weekday

number_predict_days
# we can repeat the 7 days results by np.tile
dummpy_result = np.tile(weekday_pred_visit_dummy, 2) # repeat 2 times
list(dummpy_result[0])
number_predict_days // 7 + 1 # number of weeks, that we need to repeat
dummpy_result = np.tile(weekday_pred_visit_dummy, number_predict_days // 7 + 1)
len(dummpy_result[0]) # should have length > number_predict_days (Ex: = 63)

# Now apply these to a small portion (first 1000) of real data
weekday_visit_a_small = weekday_visit_mean_align[:1000]
weekday_pred_visit_small = np.roll(weekday_visit_a_small, 
                                   -first_predict_weekday, axis = 1)
weekday_pred_visit_small
weekday_visit_a_small
weekday_visit_mean[0]
plt.plot(weekday_visit_mean[500])
plt.plot(weekday_visit_mean_align[500])
plt.plot(weekday_visit_a_small[500])
list(weekday_visit_mean[500])
list(weekday_visit_mean_align[500])

plt.plot(weekday_visit_mean[500])
plt.plot(visit[500][7:14])

# repeat data for several weeks (number_predict_days // 7 + 1)
result_small = np.tile(weekday_pred_visit_small, number_predict_days // 7 + 1)
result_small
weekday_pred_visit_small
len(result_small[0])
plt.plot(weekday_pred_visit_small[500])
plt.plot(result_small[500])
plt.show()
"""



# -- Old code --
