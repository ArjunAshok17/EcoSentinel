"""
    Self-Referential feature evolution model.
"""

from data_engineering import *      # for working with data
from visualizations import *        # for testing model

import numpy as np
from sklearn import linear_model
from math import floor


# set params #
global weight_distribution
global time_frame_ratio
global cur_val
global cur_date
global pred_range


# conduct algorithm #
def self_contained_regression(dir, feature_name, weights, time_ratio, pred_yrs):
    # params #
    set_params(weights, time_ratio, pred_yrs)
    regr_looks = []

    # import #
    feature_data = feature_import(dir, feature_name)

    col_labels = feature_data[0]
    data = feature_data[1]
    feature_output = format_data(feature_data[2])
    
    global cur_date
    cur_date = feature_data[3][0]
    global cur_val
    cur_val = feature_data[3][1]

    # time frames #
    time_frames = split_time_frame(time_data=data, frame_ratio=time_frame_ratio)
    
    # train models #
    regr_looks = train_regr_looks(time_frames=time_frames, input=data, output=feature_output, fix=False)

    # multi-regressive model #
    self_regr = regr_weighted(regr_looks=regr_looks, weight_distribution=weight_distribution)
    
    # predictions #
    regr_preds = regr_prediction(regr_looks=regr_looks, input=data, time_frames=time_frames)

    self_pred_data = np.arange(cur_date, int(cur_date + pred_range)).reshape(-1, 1)
    self_pred = self_regr.predict(self_pred_data)

    # visualize #
    plot_feature_looks(regr_preds=regr_preds, self_pred=self_pred, input=data, output=feature_output, pred_data=self_pred_data,\
                       time_frames=time_frames, col_labels=col_labels)
    
    # return outputs #
    return [ self_regr, self_pred ]


# weighted distribution of regressive looks #
def regr_weighted(regr_looks, weight_distribution):
    # apply weighting #
    self_coef = []
    sum_weights = np.sum( np.array(weight_distribution) )

    for look_num in range(len(regr_looks)):
        self_coef.append( weight_distribution[look_num] * regr_looks[look_num][0] )
    
    # averaging #
    self_coef = np.array([ np.asarray(self_coef).mean(axis=0) ]) / sum_weights

    # return model #
    self_regr = linear_model.LinearRegression()
    self_regr.coef_ = self_coef
    self_regr.intercept_ = cur_val

    return self_regr


# conducts predictions for all models #
def regr_prediction(regr_looks, input, time_frames):
    # make prediction #
    regr_preds = []

    for look_num in range(len(time_frames)):
        regr_look_info = regr_looks[look_num]
        regr_look = linear_model.LinearRegression()

        regr_look.coef_ = np.array([regr_look_info[0]])
        regr_look.intercept_ = np.array([regr_look_info[1]])

        regr_preds.append(regr_look.predict(input[ : time_frames[look_num]]))

    # return regressive predictions #
    return regr_preds


# train regressive looks #
def train_regr_looks(time_frames, input, output, fix):
    """
        add trained model for each regressive look:
              regr_look[i]      = ith regressive output
              regr_look[i][0]   = ith regressive output's coefficient coefficient
              regr_look[i][1]   = ith regressive output's intercept
    """
    regr_looks = []
    
    for frame in time_frames:
        model_info = optimize( input[ : frame], output[ : frame], cur_val=output[frame - 1][0], fix_intercept=fix )
        regr_looks.append([ model_info[1][0], model_info[2] ])
    
    return np.array(regr_looks)


# create custom weighting based on predictive range #
def distribute_weights(pred_range, skew, num_timeframes):
    """
        This will eventually replace the need to pass in weights and timeframe ratios.
        pred_range: number of time units to predict to
        skew:       -1 is left (longer term) skew,
                    0 is normal curve,
                    1 is right (shorter term skew)
    """
    # to be implemented #
    return weight_distribution


# divide data into time frames #
def split_time_frame(time_data, frame_ratio):
    # range #
        # begin = np.min(time_data)
        # end = np.max(time_data)
        # range = end - begin
    range = len(time_data)

    # divide #
    return [ floor(ratio * range) for ratio in frame_ratio ]


# sets global parameters #
def set_params(weights, time_ratio, pred_yrs):
    """
        weights:    distribution of weights along each time frame
        time ratio: ratio of time units for each time frame
        pred_yrs:   number of years to forecast to
    """
    global weight_distribution
    weight_distribution = weights

    global time_frame_ratio
    time_frame_ratio = time_ratio

    global pred_range
    pred_range = pred_yrs * 365


# divide data into time frames #
def split_time_frame(time_data, frame_ratio):
    # range #
    begin = np.min(time_data)
    end = np.max(time_data)
    range = end - begin

    # divide #
    return [ratio * range for ratio in frame_ratio]


"""
    Regression calculation.
"""
# returns optimized linear model #
def optimize(input, exp_out, cur_val, fix_intercept):
    # model creation #
    regr_look = linear_model.LinearRegression(fit_intercept=(not fix_intercept))
    if fix_intercept:
        exp_out = exp_out - cur_val
    
    # train #
    regr_look.fit(input, exp_out)

    # return model & parameters #
    return [ regr_look, regr_look.coef_[0], cur_val if fix_intercept else regr_look.intercept_[0] ]

