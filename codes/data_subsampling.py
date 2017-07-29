# -*- coding: utf-8 -*-

#import numpy as np
import pandas as pd

def data_sample(datafile = 'train_1', sample_number = 1000, 
                random_state = 1234, tag = 'sample'):
    print('Reading data ', datafile, '.csv ...', sep = '', end = '')
    df = pd.read_csv('../data/' + datafile + '.csv')
    print('done!')
    df_sample = df.sample(n = sample_number, random_state = random_state)
    df_sample.to_csv('../data/' + datafile + '_' + tag + '.csv', 
                     encoding = 'utf-8', float_format = '%d')

if __name__ == '__main__':
    data_sample()