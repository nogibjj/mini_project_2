"""
Main cli or app entry point
"""

import pandas as pd

# define a function to provide descriptive statistics of a dataset


def desripStats(file):
    # use panda to read csv file
    df = pd.read_csv(file)

    return df.describe()
