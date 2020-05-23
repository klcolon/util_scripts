import numpy as np

def cohens_d(x, y):
    """This function will calculate the effect size between two distributions. This
    function is set to accommodate unequal sample sizes.
    
    Parameters
    ----------
    x = array
    y = array
    """
    
    #calculate numerical measures
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = np.std(x)
    y_std = np.std(y)
    x_n = len(x)
    y_n = len(y)
    
    #mean difference
    mean_diff = x_mean-y_mean
    
    #bessel's corrected std for different sample size
    std_pool = np.sqrt((((x_n - 1)*x_std**2) + ((y_n - 1)*y_std**2))/(x_n + y_n - 2))
    
    #calculate cohen's d
    cohens_d = mean_diff/std_pool
    
    return np.round(cohens_d, 3)