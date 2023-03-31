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
from math import floor              # time frame calculation


"""
    Multi-Regressive model, combining all feature forecasts to predict future deforestation.
"""
"""
    ======= Set Params for Testing ========
    dir             = ""        | string for the directory to source data from
    feature_set     = [""]      | features to predict and consider; num_features inferred from here; time assumed always a feature
    weight_dists    = [[#.#]]   | weight distributions for each feature in feature_set
    time_ratios     = [[#.#]]   | time frame ratios for each weight distribution in weight_dists    
    pred_yrs        = #.#       | number of years to predict to (will output predictions for every day till then)
"""
global dir
dir = "./NYSE_sample_data/prices_adjusted.csv"

global feature_set
feature_set = ["price"]
global final_feature
final_feature = "price"

global weight_dists
weight_dists = [[25, 30, 25, 20, 15, 5, 1]]
global time_ratios
time_ratios = [[1, .75, .5, .25, .1, .05, .01]]

global pred_yrs
pred_yrs = 3


# conduct algorithm #
def multi_regression():
    # check params #
    check_params()

    # declare vars #
    self_contained_models = []      # stores final models for each feature
    self_contained_forecasts = []   # stored final forecasts (for the given predictive range) for each feature

    # import #
    dataset = data_import(dir)
    col_labels = dataset[0]

    data = dataset[1]
    output = format_data(dataset[2])
    
    # build associations for each feature #
    multi_regr_model = optimize(input=data, exp_out=output, cur_val=-1, fix_intercept=False)
    multi_regr = multi_regr_model[0]

    # train self-referencing feature predictions #
    for feat_num in range(len(feature_set)):
        self_contained_out = self_contained_regression(dir,
                                                       feature_name=feature_set[feat_num],
                                                       weights=weight_dists[feat_num],
                                                       time_ratio=time_ratios[feat_num],
                                                       pred_yrs=pred_yrs
                                                      )
        self_contained_models.append(self_contained_out[0])
        self_contained_forecasts.append(self_contained_out[1])
    
    # predictions #
    forecasted_feature_data = produce_forecasted_data(forecasts=self_contained_forecasts)
    forecast_predictions = multi_regr.predict(forecasted_feature_data)

    # visualize #
    plot_forecasts(data=data, exp_out=output, future_data=forecasted_feature_data, pred_data=forecast_predictions)


# produces the final predictive dataset for all features #
def produce_forecasted_data(forecasts):
    # combine all forecasts #
    forecasted_data = np.stack(forecasts, axis=1)
    return forecasted_data


# checks params are correctly inputted #
def check_params():
    num_features = len(feature_set)

    if num_features <= 0:
        print("ERROR: positive integer number of features required")
        quit()
    
    if len(weight_dists) != num_features:
        print("ERROR: check matching length for weight_dists and feature_set")
        quit()

    if len(time_ratios) != num_features:
        print("ERROR: check matching length for time_ratios and feature_set")
        quit()

    if len(time_ratios[0]) != len(weight_dists[0]):
        print("ERROR: check matching length for weight_dists[0] and time_ratios[0]")
        quit()


"""
    Self-Referential feature evolution model.
"""
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
    Visualization functions.
"""
# plots all regressive looks #
def plot_forecasts(data, exp_out, future_data, pred_data):
    # plot data #
    plt.scatter(data, exp_out, color="black")

    # plot forecasts #
    plt.plot(future_data, pred_data, color="forestgreen", label="Multi-Regressive Forecast")

    # labels #
    plt.legend()
    plt.xlabel("features")
    plt.ylabel("model output")

    # show plot #
    plt.show()


# plots regressive looks for one feature #
def plot_feature_looks(regr_preds, self_pred, input, output, pred_data, time_frames, col_labels):
    # plot data #
    plt.plot(input, output, color="black")
    num_frames = len(time_frames)

    # draw each regressive look #
    color = iter(plt.cm.rainbow(np.linspace(0, 1, num_frames + 1)))
    for f in range(num_frames):
        c = next(color)
        plt.plot(input[ : time_frames[f] ], regr_preds[f], color=c, label=f"Regressive Look {f}")

    # draw self predictive look #
    c = next(color)
    plt.plot(pred_data, self_pred, color=c, label=f"Self-Predictive Look")

    # labels #
    plt.legend()
    plt.xlabel(col_labels[0])
    plt.ylabel(col_labels[1])

    # show plot #
    plt.show()


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


"""
    Data import & engineering functions.
"""
# full data process #
def data_import(dir):
    # load datasets #
    data, cols = read_data(dir)

    # disregard time #
    cols.remove("time")
    col_indxs = [ cols.index(col) for col in cols ]

    data = data[ : , col_indxs ]

    # split data #
    train_data, train_output = split_io(data)

    # normalize input #
    train_data = normalize(train_data)

    # return datasets #
    return [ cols, train_data, train_output ]


# full data process #
def feature_import(dir, feature_name):
    # load datasets #
    data, cols = read_data(dir)

    # focus data #
    time_indx = cols.index("time")
    feature_indx = cols.index(feature_name)
    data = data[ : , [time_indx, feature_indx] ]

    # sort data #
    data = np.flip( data[ data[:, 0].argsort() ], axis=0)

    # split data #
    time_data, feature_data = split_io(data)

    # normalize input #
    time_data = normalize(time_data)

    # find current info #
    cur_date = time_data[0][0]
    cur_val = feature_data[0]

    # return datasets #
    return [ ["date", feature_name], time_data, feature_data, (cur_date, cur_val) ]


# reads dataset #
def read_data(dir):
    # read into panda dataframe #
    data = pd.read_csv(dir, delimiter=',')

    # convert to numpy array #
    data_arr = np.array(data.values, "float")
    data_cols = data.columns.to_list()

    # give back info #
    return data_arr, data_cols


# ensure data format #
def format_data(data):
    # # check dimensions #
    # if np.atleast_2d(data).shape[0] != 1:
    #     return data
    
    # check transposing #
    if np.atleast_2d(data).shape[0] < np.atleast_2d(data).shape[1]:
        data = np.atleast_2d(data).T

    # default #
    return data


# normalize data #
def normalize(input):
    # normalize inputs #
    # input = (input - input.min(axis=0)) * 100 / (input.max(axis=0) - input.min(axis=0))
    input = (input - input.min(axis=0))

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
