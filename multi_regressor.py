"""
    This algorithm takes multiple regressive looks at the same set of data [with respect to different timeframes] 
    to generate the most accurate linear outlook for a given time period.
    
    This works by taking multiple "regressive looks" at the same dataset for long- and short-term trends and then 
    weighing the linear models using a skewed distribution to predict for a given future time period.
"""

import numpy as np                  # cleanse data
import pandas as pd                 # load dataframe
import matplotlib.pyplot as plt     # plotting functions
from sklearn import linear_model    # linear regression


"""
    Visualization functions
"""
# plot dataset & model #
def plot_whole(regr_predictions, input, output, cols):
    # variable handling #
    num_elements, num_features = np.atleast_2d(input).shape
    pred_type = cols[num_features]

    # initialize plot #
    fig, axs = plt.subplots((num_features + 1) // 2, 2)
    fig.suptitle(f"{pred_type} Prediction")

    # plot data points #
    plt_num = 0
    for ax in axs.flat:
        # check subplot size #
        if plt_num >= num_features:
            break

        # plot data #
        ax.scatter(np.atleast_2d(input)[ : , plt_num], np.atleast_2d(output)[ : , : ], color='black')
        
        # plot regressive looks #
        plot_regressive_looks(ax, regr_preds=regr_predictions, input=input)

        # labeling #
        ax.set_title(f"{pred_type} correlation w/ {cols[plt_num]}")

        # increment #
        plt_num += 1
    
    # return plot #
    return (fig, axs)


# plots all regressive looks #
def plot_regressive_looks(ax, regr_preds, input):
    # variable handling #
    num_elements, num_features = np.atleast_2d(input).shape

    # draw each prediction #
    for regr_pred in regr_preds:
        for feature in range(num_features):
            ax.plot(np.atleast_2d(input)[ : , feature], regr_pred, color='blue', linewidth=2, label='Linear')


"""
    Regression calculation
"""
# returns optimized linear model #
def optimize(input, exp_out):
    # model creation #
    regr_look = linear_model.LinearRegression()
    
    # train #
    regr_look.fit(input, exp_out)

    # return model & parameters #
    return (regr_look, regr_look.coef_)


# conducts predictions for all models #
def regr_prediction(regr_looks, input):
    # make prediction #
    regr_preds = [regr_look.predict(input) for regr_look in regr_looks]

    # return regressive predictions#
    return regr_preds


"""
    Data import functions.
"""
# full data process #
def data_import(dir, cols):
    # load datasets #
    data = read_data(dir, cols)
    train_data, test_data, cv_data = split_data(data)

    # split data #
    train_input, train_exp_output = split_io(train_data)
    test_input, test_exp_output = split_io(test_data)
    cv_input, cv_exp_output = split_io(cv_data)

    # normalize input #
    train_input = normalize(train_input)
    test_input = normalize(test_input)
    cv_input = normalize(cv_input)

    # return datasets #
    return [train_input, train_exp_output, test_input, test_exp_output, cv_input, cv_exp_output]


# reads dataset #
def read_data(dir, cols):
    # read into panda dataframe #
    data = pd.read_csv(dir, ',', usecols=cols)

    # convert to numpy array #
    data_arr = np.array(data.values, 'float')

    # give back info #
    return data_arr


# ensure data format #
def format_data(data):
    # check transposing #
    if np.atleast_2d(data).shape[0] < np.atleast_2d(data).shape[1]:
        data = np.atleast_2d(data).T

    # default #
    return data


# normalize data #
def normalize(data):
    # normalize inputs #
    input = input / input.max(axis=0)

    # return split data #
    return input


# split data into input & output #
def split_io(data):
    # dimensions #
    num_elements, num_features = data.shape
    num_features -= 1

    # split data #
    input = np.atleast_2d(data)[ : , : num_features]
    expected_output = np.atleast_2d(data)[ :, num_features]

    # return split #
    return input, expected_output


# splits into training, test, and cross-validation sets #
def split_data(data):
    # dimensions #
    num_elements, num_features = np.atleast_2d(data).shape

    # percent split #
    train_entries = int(num_elements * .7)
    test_entries = int(num_elements * .15)
    cv_entries = num_elements - (train_entries + test_entries)

    test_start = train_entries + 1
    cv_start = train_entries + test_entries + 1

    # randomize #
    np.random.shuffle(data)

    # split #
    train_data = np.atleast_2d(data)[ : test_start, : ]
    test_data = np.atleast_2d(data)[test_start : cv_start, : ]
    cv_data = np.atleast_2d(data)[cv_start : , : ]

    # return #
    return train_data, test_data, cv_data
