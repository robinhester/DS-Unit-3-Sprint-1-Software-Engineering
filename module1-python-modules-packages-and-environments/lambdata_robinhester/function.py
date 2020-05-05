# creating an accuracy score for model configuration
import numpy


def accuracy_score(x, y):
    '''
    Used for comparing the actual values of a model to the predicted
    values of a model

    Params: Two values. X as the actual values, in a list or series form.
    Y as the predicted values, in a list or series form.

    Example: a_list=pd.Series([2039, 4992, 8906, 12094])
             b_list=pd.Series([2039,4000,8000,12098])

    Returns: Percent of Average Correct Information

    Note: x must be the actual values

    '''
    errors = abs(y-x)
    accuracy_mean = numpy.mean(100*(errors/x))
    score = 100-accuracy_mean

    return(score)
