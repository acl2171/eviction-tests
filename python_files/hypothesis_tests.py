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

def create_sample_dists(sample1, sample2, y_var=None):
    """
    This function creates a histogram in seaborn with the given data and y_variable. 

    :param cleaned_data: a dataframe
    :param y_var: The numeric variable you are comparing (column name)
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    return (plt.figure(figsize = (10, 6)), sns.distplot(sample1[y_var]), sns.distplot(sample2[y_var]))

def create_PUD_variable_and_samples(dataframe, ):
    """This function creates a pud variable and two samples.
    It returns a list of two dataframes representing the two samples to be tested."""
    dataframe['PUD'] = [0 if x==True else 1 for x in dataframe['PUD_NAME'].isna()]
    with_PUDS = (dataframe[dataframe['PUD'] == 0])
    no_PUDS = dataframe[dataframe['PUD']==1]
    return [with_PUDS, no_PUDS]

def hypothesis_test_one(sample1, sample2, variable = None, alpha = 0.05):
    """Hypothesis Test I runs a two-sample t-test from scipy.stats and returns a list of the test statistic and pvalue.
    :param alpha: the critical value of choice (default 0.05)
    :param sample1: dataframe
    :param sample2: dataframe
    :variable: the column of choice for the hypothesis test
    :return: list of t-statistic and p-value, and string interpreting results"""
    result = stats.ttest_ind(sample1[variable], sample2[variable], equal_var = False)
    if result[1] < alpha:
        return result, "The p-value is less than alpha; therefore, we reject the null hypothesis."
    else:
        return result, "The p-value is greater than alpha; therefore we fail to reject the null hypothesis."
        
        
        
# def hypothesis_test_two():
#     pass
