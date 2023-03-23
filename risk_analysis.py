"""
    This algorithm takes the results of the multi-regressive time series analysis to calculate future risk of
    a specific ecosystem being damaged beyond the point of recovery.

    The assumption being made is that all features will have been previously normalized & flipped so that 
    positive 1 is always high correlation with deforestation (for each feature) and negative one is always 
    a high corrrelation with reforestation. This assumption will be enforced in the program.
"""

import numpy as np                  # arrays and data manipulation 
import pandas as pd                 # working with data i/o
from sklearn import linear_model    # predictive analytics


"""
    Define variables & constants used throughout the program
"""
dir = "Users/arjun/..."                 # directory for input data
cols = ["countries", "regr_coef"]       # dataset labels
output_dir = "User/arjun/..."           # directory for output
risk_proj_year = 5                      # number of years to gauge risk from

# # dictionary associating each feature with a weight for risk #
# risk_factors = {
#     # "feature" : weight_asfloat #
#     # total weight should add to 1.0 #
#     "forest_cover" : .7,
#     "avg_temp" : .3
# }


"""
    Load data, conduct analysis, and export data
"""
def main(void):
    # load data #
    data = pd.read_csv(dir, ',', usecols=cols)
    countries = data[0]
    regr_trends = data[1]

    # calculate risk #
    risk_analysis = calc_risk(regr_trends)

    # create data frame #
    risk_df = np.vstack(countries, risk_analysis).T

    # deploy data #
    risk_df.to_csv(dir, columns=["countries", "projected_risk"])


"""
    The assumption being made is that all features will have been previously normalized & flipped so that 
    positive 1 is always high correlation with deforestation (for each feature) and negative one is always 
    a high corrrelation with reforestation.
    
    In order to enforce this rule, we force the normalization and conversion ourselves, assuming that the 
    models that were trained have a different min/max for correlation and therefore the 
"""
def enforce_data(dataset):
    # normalize dataset #
    dataset = dataset / dataset.max(axis=0)

    # conversion #
    

"""
    Risk analysis calculations

    Risk will be highly dependent on long- and short-term trends, so we need a way of taking the final result
    from the multi-regressor to predict future growth and then calculate a range of error and final risk.

    Risk will be normalized prior to the final calculation by standardizing the regressive coefficients.
"""
def calc_risk(multi_regr_coef, forest_covers):
    # define risk factors #
    risks = []
    # risk_weights = np.fromiter(risk_factors.values(), dtype=float)

    # risk formula #
    for coef in multi_regr_coef:
        # predict #
        model = linear_model.LinearRegression()
        model.coef_ = coef
        projection = model.predict()

        # distribute weights & sum result #
        risk = np.sum(np.multiply(risk_weights, np.multiply(num_years, coef))

        # add other factors #
        

        # add risk #
        risks += [risk]
        
    # output risks #
    return risks

