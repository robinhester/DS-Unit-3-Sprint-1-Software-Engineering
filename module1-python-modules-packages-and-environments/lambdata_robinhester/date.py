import pandas as pd
import datetime as dt


def date_conversion(X):
    """
    Takes a column of date information and converts 
    it to pandas datetime values then splits up year 
    day and month into new columns

    Param: must have datelike type information in pandas series format

    Example:

    Returns: 3 new columns, Year, Day, and Month, 
    added into the original dataframe
    """
    X = pd.to_datetime(X)
    X['Year'] = X.dt.year
    X['Day'] = X.dt.day
    X['Month'] = X.dt.month

    return(X)
