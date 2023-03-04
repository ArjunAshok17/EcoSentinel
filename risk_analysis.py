"""
    This algorithm takes the results of the multi-regressive time series analysis to calculate future risk of
    a specific ecosystem being damaged beyond the point of recovery.
"""

import numpy as np      # arrays and data manipulation 
import pandas as pd     # working with data i/o


"""
    Load data, conduct analysis, and export data
"""
def main(void):
    # load data #



"""
    Risk analysis calculations

    Risk will be highly dependent on long- and short-term trends, so we need a way of taking the final result
    from the multi-regressor to predict future growth and then calculate a range of error and final risk.

    Risk will not be normalized, ensuring each country is accurately depicted with risk.
"""
def calc_risk(multi_regr_coef):
    # risk coefficients #
    

    # risk formula #
    for coef in 


"""
    Data import functions.
"""
# reads dataset #
def read_data(dir, cols):
    # read into panda dataframe #
    data = pd.read_csv(dir, ',', usecols=cols)

    # convert to numpy array #
    data_arr = np.array(data.values, 'float')

    # give back info #
    return data_arr