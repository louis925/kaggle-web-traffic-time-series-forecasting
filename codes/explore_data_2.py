# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import data_processing as dp

print('Reading data...', end = '')
dates, page, visit, key, predict_dates, readin = dp.read_data()
print('done!')

n_days = len(visit[0])
print('Number of days:', n_days)
print('visit[0]', visit[0])

n_page = len(page)
print('Number of pages:', n_page)
print(page)

dp.plot_some_visit(visit, page)
dp.plot_visit(103351, visit, page)

i = 103351
plt.figure(1, figsize = (10, 6))
plt.plot(visit[103351])
plt.plot(visit[103352])
plt.show()

np.savetxt('single_data ' + str(i) + '.csv', visit[i], delimiter = ',')

readin_subsample = readin.sample(n = 1000)
readin_subsample.to_csv('../data/train_1_subsample.csv', encoding='utf-8')
