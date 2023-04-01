"""
    This algorithm takes the results of the multi-regressive time series analysis to assign a grade
    to countries based on their efforts in protecting the natural landscapes within their borders.

    This algorithm only considers one country at a time. To run against multiple countries, you will 
    have to call it against each one in a separate script/program.
"""

from self_ref_regressor import *        # gauge trends in risk


"""
    Define variables & constants used throughout the program
"""
dir = ""                                                                # directory for input data for risks over times


"""
    Load data, conduct analysis, and export results
"""
def grade_calc():
    # gauge risk trends #
    risk_trend = self_contained_regression(dir=dir, feature_name="risks", weights=[5, 10, 20, 40, 20, 15], 
                                           time_ratio=[1, .5, .25, .125, .0625, 0.03125], pred_yrs=3)
    
    risk_prediction = risk_trend[1][-1]     # get last predicted risk value

    # gauge legislative trends #
    legislative_trend = calc_legislative_trend()

    # calculate grade #
    return calc_grade(risk=risk_prediction, leg_effort=legislative_trend)


"""
    Grade calculations
"""
def calc_grade(risk, leg_effort):
    # define grade parameters #
    w_leg = 25.0                # weighting constant for legislative efforts in the grade calculation
    w_risk = -50.0              # weighting constant for risk trends in the grade calculation
    grade_offset = 75.0         # default grade given perfectly neutral parameters
    max_risk = 200.0            # max risk value that can be assigned

    # calculate risk #
    grade = grade_offset + w_leg * leg_effort + w_risk * ( float(risk) / max_risk )
    final_grade = match_grade(grade=grade)
        
    # output grade #
    return final_grade


def match_grade(grade):
    if grade >= 97:
        return "A+"
    elif grade >= 93:
        return "A"
    elif grade >= 90:
        return "A-"
    elif grade >= 87:
        return "B+"
    elif grade >= 83:
        return "B"
    elif grade >= 80:
        return "B-"
    elif grade >= 77:
        return "C+"
    elif grade >= 73:
        return "C"
    elif grade >= 70:
        return "C-"
    elif grade >= 67:
        return "D+"
    elif grade >= 63:
        return "D"
    elif grade >= 60:
        return "D-"
    return "F"


"""
    The legislative analysis will be implemented in the future, we are just laying out the 
    framework right now for future expansion.

    Read the comment in legislation_analysis.py for further info
"""
def calc_legislative_trend():
    return 0

