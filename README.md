# Kaggle - Web Traffic Time Series Forecasting #
  
This repository contains the codes to solve the Kaggle competition "Web traffic time series forecasting" (https://www.kaggle.com/c/web-traffic-time-series-forecasting).

### Contributors ###
Louis Yang (github.com/louis925)

Chen-Hsi (Sky) Huang (github.com/skyhuang1208)   

### Achievement ###
11th place out of 1095 teams (Gold medal, top 2%) on stage 2 private leaderboard with SMAPE score 37.919.

### How to Use ###
1. Download this repository.
2. Download and unzip the training data `train_2.csv.zip` and `key_2.csv.zip` from Kaggle website (https://www.kaggle.com/c/web-traffic-time-series-forecasting/data). Place them in the `data` directory. Rename `train_2.csv` to `train_3.csv`.
3. Run `main.ipynb` in the `codes` directory to generate prediction in the `results` directory.

### How it works ###
We use a Fibonacci series as the window sizes to compute the a serie of median excluding nan for each sample (page). Then find again the median amount the series excluding nan. Use this median-median (which we call Fibonacci median) as the center of each sample. The Fibonaccis series we took is `[11, 18, 30, 48, 78, 126, 203, 329]`, which was suggested by Ehsan  http://www.kaggle.com/safavieh/median-estimation-by-fibonacci-et-al-lb-44-9?scriptVersionId=1466647 and has original scored 44.9 in the stage 1 Kaggle leaderboard.

To better train the neural network for various scales of dayily visits, we first do the log1p transformation in the form 
    
    X_log = log10(X_ori + 1),

to bring them into the same order. Then we sample-wise (page-wise) standardize the data using the Fibonacci median (`fib_med`) instead of regular mean as the center baseline and the usual standard deviation (`stdev`) as the scale, where `nan` is treated as `0`.

According to the Fibonacci median (`fib_med`), we split data (pages) into groups and train individual neural network (models) in each group. The group spliting is determined by 

    log10(fib_med + 1) < (1.0, 2.0, 4.0, greater)
    
So there are total 4 groups.

The first group (group 0) use the result from the Fibonacci median model (`fib_med`) since it is difficult to learn by our neural network. For the rest groups (group 1-3), we use the results from the convolutional neural network (CNN). 

The neural network takes 64 days (`x_length`) of data and predicts the following 64 days (`y_length`) of results. For the neural network structure, we use single 1D convolutional layer with 140 neurons, kernel size 3, and relu activation function, which pass through average pooling with size 2. After the flatten the convolutional result, we feed the Fibonacci median and stdev (after log transform) for the sample as addional inputs via concatenation. Finally, the concatenated data is pass into 3 fully connected layer (130, 120, and 64 neurons) with 2 relu and 1 linear activation functions to do the regression. 

The CNN structure is: 

    [X > Conv1D(140, kernel=3) > AvgPool(2) > Flat + Additional input, A, (median, stdev)] > Concat > 
    FC(130, relu) > FC(120, relu) > FC(64, linear) > Y

Ensemble learning: We train the same neural network 5 times. Each run only train on 4/5 of the data. Then we take the median of the result from each run.

Group model optimization: We evaluate the group models (neural network trained within their own group) on other groups data, and assign their results based on their performance in test mode. Since in the test (validation) mode the neural network model trained by group 2 do better than those trained by group 3 on group 3 data, we use the group model 2 for predicting group 3 result.
