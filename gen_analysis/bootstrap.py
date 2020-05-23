import numpy as np

class bootstrap:
    def draw_sample(data):
        """Draw a bootstrap sample from a 1D data set."""
        return np.random.choice(data, size=len(data))

    def draw_reps(data, test_statistic = "mean", size=1):
        """Draw boostrap replicates from 1D data set. Default is set to mean, otherwise, it will be median.
        Parameters
        ----------
        data = 1D dataset
        test_statistic = median or mean
        size = integer

        Returns
        -------
        numpy array of bootstrap replicates
        """
        if test_statistic == "mean":
            out = np.empty(size)
            for i in range(size):
                out[i] = np.mean(draw_bs_sample(data))
        else:
            out = np.empty(size)
            for i in range(size):
                out[i] = np.median(draw_bs_sample(data))

        return out 

    def confidence_interval(data):
        """Return 95% confidence interval for boostrap replicates"""
        return np.percentile(data, [2.5, 97.5])
