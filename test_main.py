"""
Test goes here

"""

from main import desripStats, findMin, findMax, calcMean
import pandas as pd


def test_pd_descriptive():
    # dataset file
    file = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"

    print("this code reads csv data from: ", file)

    data_summary = desripStats(file)

    # data = pd.read_csv(file)["mpg"]

    # run some test cases: mean, min and max of the 'mpg'
    # minimum
    # try:
    #     min_mpg = findMin(data)
    #     assert data_summary["mpg"]["min"] == min_mpg
    # except AssertionError as msg:
    #     raise msg + "minimum result unmatch"

    # # maximum
    # try:
    #     max_mpg = findMax(data)
    #     assert data_summary["mpg"]["max"] == max_mpg
    # except AssertionError as msg:
    #     raise msg + "maximum result unmatch"

    # # mean
    # try:
    #     mean_mpg = calcMean(data)
    #     assert round(data_summary["mpg"]["mean"], 3) == mean_mpg
    # except AssertionError as msg:
    #     raise msg + "mean result unmatch"


if __name__ == "__main__":
    test_pd_descriptive()
