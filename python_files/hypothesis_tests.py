"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math
import seaborn as sns
import matplotlib.pyplot as plt

def create_PUD_variable_and_samples(dataframe, ):
    """This function creates a pud variable and two samples.
    It returns a list of two dataframes representing the two samples to be tested."""
    # if no PUD exists(null), code 0. Code 1 if PUD exists
    dataframe['PUD'] = [0 if x==True else 1 for x in dataframe['PUD_NAME'].isna()]
    no_PUDS = (dataframe[dataframe['PUD'] == 0])
    with_PUDS = dataframe[dataframe['PUD']==1]
    return [with_PUDS, no_PUDS]

def create_Pov_variable_and_samples(dataframe, ):
    """This function creates a poverty variable and two samples.
    It returns a list of two dataframes representing the two samples to be tested."""
    # check summary statistics
    pov_mean0 = dataframe['poverty-rate'].mean()
    pov_std0 = dataframe['poverty-rate'].std()
    
    # establish bounds for outliers and drop outliers
    outlier_lower = pov_mean0 - 1.5*pov_std0
    outlier_upper = pov_mean0 + 1.5*pov_std0
    pov_df = dataframe.loc[~((dataframe['poverty-rate'] > outlier_upper) | (dataframe['poverty-rate'] < outlier_lower))]
    
    # recheck summary statistics
    pov_mean1 = pov_df['poverty-rate'].mean()
    pov_std1 = pov_df['poverty-rate'].std()
    
    # add column with poverty quintiles
    pov_df['poverty_cat'] = np.where(pov_df['poverty-rate'] > (pov_mean1 + pov_std1), 'high',
                         np.where(pov_df['poverty-rate'] > (pov_mean1), 'somewhat high', 
                         np.where(pov_df['poverty-rate'] < (pov_mean1 - pov_std1), 'low',
                         np.where(pov_df['poverty-rate'] < (pov_mean1), 'somewhat low', np.nan))))
    
    higher = pov_df.loc[pov_df['poverty_cat'] == 'high']
    lower = pov_df.loc[pov_df['poverty_cat'] != 'high']
    return [higher, lower]

def hypothesis_test(sample1, sample2, variable = None, type = 'two-sided', alpha = 0.05):
    """Hypothesis Test I runs a two-sample t-test from scipy.stats and returns a list of the test statistic and pvalue.
    :param alpha: the critical value of choice (default 0.05)
    :param sample1: dataframe
    :param sample2: dataframe
    :param variable: the column of choice for the hypothesis test
    :param type: string, whether the test is one-sided or two-sided
    :return: list of t-statistic and p-value, and string interpreting results"""
    result = stats.ttest_ind(sample1[variable], sample2[variable], equal_var = False)
    pvalue = result[1]
    if type=='one-sided':
        pvalue = pvalue/2
    else:
        pvalue
    if pvalue < alpha:
        return result, "The p-value is less than alpha; therefore, we reject the null hypothesis."
    else:
        return result, "The p-value is greater than alpha; therefore we fail to reject the null hypothesis."
        
def calculate_cohen_d(sample1, sample2, variable = None):
    """This function calculates cohen's D when given two samples.
    :param sample1: dataframe
    :param sample2: dataframe
    :param variable: name of column of interest
    :returns a floating point number"""
    group1 = sample1[variable]
    group2 = sample2[variable]
    
    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    # Calculate the pooled threshold
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    
    # Calculate Cohen's d statistic
    d = diff / np.sqrt(pooled_var)
    
    return "Cohen's D: {}".format(d)