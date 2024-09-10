"""
Test goes here

"""

from main import desripStats, findMin  # , findMax, calcMean
import pandas as pd
import requests


def check_url_exists(url):
    try:
        # Send a GET request to the URL
        response = requests.head(url, allow_redirects=True)

        # Check if the status code is in the range of success codes (200-299)
        if 200 <= response.status_code < 300:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network problems, invalid URL, etc.)
        print(f"Error occurred: {e}")
        return False


# run some test cases: mean, min and max of the 'mpg'
# minimum
def test_findMin(file):
    data = pd.read_csv(file)["mpg"]
    min_mpg = findMin(data)
    return min_mpg


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
    url = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    assert check_url_exists(url)
    dataframe = pd.read_csv(url)
    # test findMin
    assert test_findMin(url) == desripStats(dataframe)["mpg"]["min"]
    # test findMax
    # assert findMax(data) == 33.9
    # # test calcMean
    # assert calcMean(data) == 20.091
