# -*- coding: utf-8 -*-
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

submission_file = 'submit_1_model_10_Modified_CNN_4_The_Model_1_stage_1_predict.csv'

correct_file = 'submit_1_stage_1_correct.csv'

print('%%% Reading submission', submission_file, '... ', end = '', flush = True)
submit_df = pd.read_csv('../results/' + submission_file)
print('done!')

print('%%% Reading submission', correct_file, '... ', end = '', flush = True)
correct_df = pd.read_csv('../results/' + correct_file)
print('done!')

print('Head of the submit file:')
print(submit_df.head())

print('Head of the correct result:')
print(correct_df.head())

# Check Id
submit_id = submit_df['Id']
correct_id = correct_df['Id']

print('Id align:', (submit_id == correct_id).all())

def smape(y_true, y_pred, axis=None):
    '''Symmetric mean absolute percentage error'''
    diff = np.abs((y_true - y_pred) / 
                  np.clip(np.abs(y_true) + np.abs(y_pred), 1e-7,
                          None))
    return 200. * np.nanmean(diff, axis=axis)

y_submit = submit_df['Visits'].values
y_correct = correct_df['Visits'].values

print('SMAPE:', smape(y_correct, y_submit))
