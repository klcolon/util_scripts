import numba 
import numpy as np

@numba.njit

def draw_perm_sample(x, y):
    """Generate a permutation sample.
    
    Parameters
    ----------
    x = 1D array
    y = 1D array"""
    
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    concat_data = np.concatenate((x, y))
    np.random.shuffle(concat_data)

    return concat_data[:len(x)], concat_data[len(x):]

def draw_perm_reps_diff_mean(x, y, size=1):
    """Generate array of permuation replicates.
    
    Parameters
    ----------
    x = 1D array
    y = 1D array"""
    
    x = x[~np.isnan(x)]
    y = y[~np.isnan(y)]
    out = np.empty(size)
    for i in range(size):
        x_perm, y_perm = draw_perm_sample(x, y)
        out[i] = np.abs(np.mean(x_perm) - np.mean(y_perm))

    return out