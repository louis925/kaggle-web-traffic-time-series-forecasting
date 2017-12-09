# -*- coding: utf-8 -*-
# This script samples the training data (train_1.csv) to reduce the size

#import numpy as np
import pandas as pd

def data_sample(datafile = 'train_1', sample_number = 20000, 
                random_state = 1234, tag = 'sample', path = '../data/'):
    print('Reading data ', datafile, '.csv ...', sep = '', end = '')
    df = pd.read_csv(path + datafile + '.csv')
    print('done!')
    df_sample = df.sample(n = sample_number, random_state = random_state)
    out_filename = datafile + '_' + tag + '.csv'
    print('Writing sample data ', out_filename, ' ...', sep = '', end = '')
    df_sample.to_csv(path + out_filename, 
                     encoding = 'utf-8', float_format = '%d')
    print('done!')    

if __name__ == '__main__':
    data_sample(tag = 'sample_2')