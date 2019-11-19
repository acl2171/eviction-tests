"""

### Visualizations

This module contains the functions for all the visualizations for our project.

"""
import seaborn as sns
import matplotlib.pyplot as plt

def create_sample_dists(sample1, sample2, y_var=None):
    """
    This function creates a histogram in seaborn with the given data and y_variable. 

    :param cleaned_data: a dataframe
    :param y_var: The numeric variable you are comparing (column name)
    :param categories: the categories whose means you are comparing
    :return: image of two datasets plotted on a histogram

    """
    figure = plt.figure(figsize = (10, 6))
    return (sns.set_context('talk'), plt.figure(figsize = (10, 6)), sns.distplot(sample1[y_var], color = 'magenta'), sns.distplot(sample2[y_var], color = 'gray'))

