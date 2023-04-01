"""
    This algorithm takes the results of the multi-regressive time series analysis to calculate future risk of
    a specific ecosystem being damaged beyond the point of recovery.

    The assumption being made is that all features will have been previously normalized & flipped so that 
    positive 1 is always high correlation with deforestation (for each feature) and negative one is always 
    a high corrrelation with reforestation. This assumption will be enforced in the program.
"""

import numpy as np                  # arrays and data manipulation 
import pandas as pd                 # working with data i/o


"""
    Define variables & constants used throughout the program
"""
dir = ""                                                                # directory for input data
cols = ["countries", "proj_forest_cover", "min_recorded_cover"]         # dataset labels
output_dir = ""                                                         # directory for output


"""
    Load data, conduct analysis, and export data
"""
def risk():
    # load data #
    data = pd.read_csv(dir, ',', usecols=cols)
    countries = data[0]
    proj_for_covs = data[1]
    min_recorded_covs = data[2]

    # calculate risk #
    risk_analysis = calc_risk(proj_forest_covers=proj_for_covs, min_forest_covers=min_recorded_covs)

    # create data frame #
    risk_df = np.vstack(countries, risk_analysis).T

    # deploy data #
    risk_df.to_csv(output_dir, columns=["countries", "projected_risk"])


"""
    Risk analysis calculations

    Risk will be highly dependent on long- and short-term trends, so we need a way of taking the final result
    from the multi-regressor to predict future growth and then calculate a range of error and final risk.

    Risk will be normalized prior to the final calculation by standardizing the regressive coefficients.
"""
def calc_risk(proj_forest_covers, min_forest_covers):
    # define risk #
    alpha_neg = 1.0             # proportional constant in case risk needs to be shifted
    alpha_pos = 1.0             # proportional constant in case risk needs to be shifted
    risks = []                  # risks for each country specified

    # calculate risk #
    for proj_cov, min_cov in zip(proj_forest_covers, min_forest_covers):
        if min_cov >= proj_cov:
            risk = 100 + ( float(min_cov - proj_cov) / min_cov ) * 100
            risk *= alpha_neg
        else:
            risk = 1 / ( (float(proj_cov - min_cov) / proj_cov) + 1)
            risk *= alpha_pos
        
    # output risks #
    return risks


"""
    We have reached out to Envrironmental Science professors to try and come up
    with a formula to estimate the minimum viable forest cover that defines the min 
    forest cover for which most forest (and later other) ecosystems can fully rebound 
    from without additional human aid.

    In other words, this is the minimum area needed for nature to solve the 
    deforestation problem on its own. Past this point, serious effort will be needed.

    This formula is yet to be finalized, so for now we are making the assumption that 
    for any given forest data, its minimum point has thus far been recoverable (unless 
    the minimum point is the current point). Therefore, we will use the minimum recorded 
    data point until a better formula can be agreed upon.
"""
def calc_min_viable_cover(forest_data):
    # variable defining #
    min_historical_cov = np.min(forest_data)

    # formula (yet to be finalized) #
    min_viable_cov = min_historical_cov

    return min_viable_cov

