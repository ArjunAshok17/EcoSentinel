"""
    This algorithm takes multiple regressive looks at the same set of data [with respect to different timeframes] 
    to generate the most accurate linear outlook for a given time period.
    
    This works by taking multiple "regressive looks" at the same dataset for long- and short-term trends and then 
    weighing the linear models in a balanced weigh to predict for a given future time period.
"""

import numpy as np                  # cleanse data
import pandas as pd                 # load dataframe
from sklearn import linear_model    # linear regrssion
from data_management import *       # data management


"""
    Regression calcualtion
"""
# returns optimized linear model #
def optimize(input, exp_out):
    # model creation #
    regr_look = linear_model.LinearRegression()
    
    # train #
    regr_look.fit(input, exp_out)

    # return model & parameters #
    return (regr_look, regr_look.coef_)


"""
    Data import functions.
"""
# full data import #
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


# normalize data #
def normalize(data):
    # split data #
    input, expected_output = split_io(data)

    # normalize inputs #
    input = input / input.max(axis=0)

    # return split data #
    return input, expected_output


# split data into input & output #
def split_io(data):
    # dimensions #
    num_entries, num_cols = data.shape
    num_cols -= 1

    # split data #
    input = data[ : , : num_cols]
    expected_output = data[ :, num_cols]

    # return split #
    return input, expected_output


# splits into training, test, and cross-validation sets #
def split_data(data):
    # dimensions #
    num_entries, num_cols = data.shape

    # percent split #
    train_entries = int(num_entries * .7)
    test_entries = int(num_entries * .15)
    cv_entries = num_entries - (train_entries + test_entries)

    test_start = train_entries + 1
    cv_start = train_entries + test_entries + 1

    # randomize #
    np.random.shuffle(data)

    # split #
    train_data = data[ : test_start, : ]
    test_data = data[test_start : cv_start, : ]
    cv_data = data[cv_start : , : ]

    # return #
    return train_data, test_data, cv_data
