import numpy as np
import pandas as pd

def ecdf(data, label):
    """Calculates ecdf from a 1D array
    
    Parameters
    ----------
    data = 1D array
    label = string
    
    Returns 
    Pandas dataframe with ecdf values, labels, and x values
    """
    
    data = data[~np.isnan(data)]
    ecdf = pd.DataFrame(np.arange(1, len(data)+1) / len(data))
    ecdf['Label'] = label
    ecdf['Values'] = np.sort(data)
    ecdf.columns = ["ecdf", "Label", "Values"]
    
    return ecdf
