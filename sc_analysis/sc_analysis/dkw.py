import numpy as np
import pandas as pd
import numba

@numba.njit

def ecdf(x, data):
    """Give the value of an ECDF at arbitrary points x.
    args
    ----
    x = array or int or float
    data = data used to generate ecdf"""
    
    y = np.arange(len(data) + 1) / len(data)
    return y[np.searchsorted(np.sort(data), x, side="right")]

def dkw_conf_int(x, data, alpha):
    """Compute a Dvoretzky–Kiefer–Wolfowitz inequality.
    arg
    ---
    x = array or int or float
    data = data used to generate ecdf
    alpha = confidence interval"""
    
    epsilon = np.sqrt(np.log(2/alpha) / 2 / len(data))

    ecdf_y = ecdf(x, data)

    lower_bound = np.maximum(0, ecdf_y - epsilon)
    upper_bound = np.minimum(1, ecdf_y + epsilon)
    
    return lower_bound, upper_bound