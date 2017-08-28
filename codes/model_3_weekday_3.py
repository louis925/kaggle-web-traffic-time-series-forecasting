# -*- coding: utf-8 -*-
"""
Note this is a python version of the kernel on Kaggle
This script doesn't depend on any other code
"""
print('')
print('Kaggle - Web Traffic Time Series Forecasting')
print('         by Sky Huang and Louis Yang')
model_name = 'model_03_weekday_3_median_49'
print('Model 03 - Weekday - 3 - last 49 days median')

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

print('%%% Reading data train_1.csv ...', end = '', flush = True)
train = pd.read_csv("../data/train_1.csv")
print('done!')
train_flattened = pd.melt(train[list(train.columns[-49:])+['Page']], 
                                id_vars='Page', var_name='date', 
                                value_name='Visits')
train_flattened['date'] = train_flattened['date'].astype('datetime64[ns]')
train_flattened['weekday'] = train_flattened.date.dt.dayofweek

print('%%% Reading data key_1.csv ...', end = '', flush = True)
test = pd.read_csv("../data/key_1.csv")
print('done!')

test['date'] = test.Page.apply(lambda a: a[-10:])
test['Page'] = test.Page.apply(lambda a: a[:-11])
test['date'] = test['date'].astype('datetime64[ns]')
test['weekday'] = test.date.dt.dayofweek

train_page_per_dow = train_flattened.groupby(['Page','weekday']).median().reset_index()

test = test.merge(train_page_per_dow, how='left')
test.loc[test.Visits.isnull(), 'Visits'] = 0.0

print('%%% Writing result for submodel 3 - Median last 49 days', end = '', flush = True)
test[['Id','Visits']].to_csv('../results/submit_1_' + model_name
                             + '.csv', index = False)
print('done!')
