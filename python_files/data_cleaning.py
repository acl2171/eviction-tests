"""
## DATA CLEANING

This module is for data cleaning.

# Notes:
There can be an unlimited amount of support functions.
Each support function should have an informative name and return the partially cleaned bit of the dataset.
"""

import pandas as pd

def clean_eviction_data(e_df, year, GEOIDs_list):
    """Limits dataset to a given year and list of GEOIDs"""
    df = df.loc[df.year == year]
    df = df.loc[df['GEOID'].isin(GEOIDs_list)]
    df.reset_index(inplace=True)
    return df

def merge_in_puds(e_df,p_df):
    """Merges main dataset with PUD dataset based on crosswalk"""
    crosswalk = pd.read_csv('../data/ward8PUDcrosswalk.csv')
    df = p_df.merge(crosswalk[['OBJECTID','GEOID']], on='OBJECTID')
    e_df = e_df.merge(p_df, on='GEOID')
    return e_df

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    evict = pd.read_csv("../data/EvictionLab/tracts.csv")
    puds = pd.read_csv("../data/OpenData/Planned_Unit_Development_PUDs.csv")

    evict = support_function_one(evict)
    evict = support_function_two(evict,puds)
    evict.to_csv('./data/cleaned_for_testing.csv')
    
    return evict