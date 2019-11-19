"""
## DATA CLEANING

This module is for data cleaning.

"""

import pandas as pd

def clean_eviction_data(df, year, GEOIDs_list):
    """Limits dataset to a given year and list of GEOIDs"""
    df = df.loc[df.year == year]
    df = df.loc[df['GEOID'].isin(GEOIDs_list)]
    df.reset_index(inplace=True)
    return df

def merge_in_puds(df,p_df):
    """Merges main dataset with PUD dataset based on crosswalk"""
    crosswalk = pd.read_csv('../data/ward8PUDcrosswalk.csv')
    p_df = p_df.merge(crosswalk[['OBJECTID','GEOID']], on='OBJECTID')
    df = df.merge(p_df, on='GEOID', how='outer')
    return df

ward8 = [11001009801,11001009802,11001009803,11001009804,11001007502,11001007503,11001007504,11001009807,11001009810,11001009811,11001009700,11001007401,11001007403,11001007404,11001007406,11001007407,11001007408,11001007409,11001007301,11001007304,11001010900,11001010400,11001007601]

def full_clean():
    """
    This is the one function called that will run all the support functions.
    Assumption: Your data will be saved in a data folder and named "dirty_data.csv"

    :return: cleaned dataset to be passed to hypothesis testing and visualization modules.
    """
    evict = pd.read_csv("../data/EvictionLab/tracts.csv")
    puds = pd.read_csv("../data/OpenData/Planned_Unit_Development_PUDs.csv")
    
    evict = clean_eviction_data(evict, 2016, ward8)
    evict = merge_in_puds(evict,puds)
    evict.drop(['index'],axis=1, inplace=True)
    evict.to_csv('../data/cleaned_for_testing.csv', index=False)
    
    return evict