# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 16:40:32 2017

@author: Louis
"""
print('')
print('Kaggle - Web Traffic Time Series Forecasting')
print('         by Sky Huang and Louis Yang')
print('Model 01 - Average')

from read_data import read_data
print('Reading data...', end = '')
dates, page, visit, key = read_data()
print('done!')

number_days = len(visit[0])
number_pages = len(page)
print('%%%%% Overview of the data: %%%%%')
print('  Number of pages:', number_pages)
print('  Number of days of data:', number_days)
print('  visit[0]:', visit[0])
print('  page[:5]', page[:5])
