import numba
import numpy as np

@numba.njit
def draw_bs_sample(data):
    """Draw a bootstrap sample from a 1D data set."""
    return np.random.choice(data, size=len(data))

def draw_bs_reps_median(data, size=1):
    """Draw boostrap replicates of the median from 1D data set."""
    out = np.empty(size)
    for i in range(size):
        out[i] = np.median(draw_bs_sample(data))
    return out 

def confidence_interval(data):
    """Return 95% confidence interval for boostrap replicates"""
    return np.percentile(data, [2.5, 97.5])
