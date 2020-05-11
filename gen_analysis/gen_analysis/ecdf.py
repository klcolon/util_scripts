import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

def plot(data, label):
    """generates ecdf plots
    
    Parameters
    ----------
    data = tidy data with values in one column and labels in another
    label = column name with categories
    
    Returns 
    ecdf plot using matplotlib
    """
    
    #obtain unique values
    labels = data[label].unique()
    
    #calculate ecdf for every label
    ecdf_list = []
    for i in labels:
        sliced_data = data.loc[data[label] == i].values
        ecdf_val = ecdf(sliced_data, i)
        ecdf_list.append(ecdf_val)
    
    #plot
    for i in range(len(ecdf_list)):
        plt.step(ecdf_list[i]["Values"], ecdf_list[i]["ecdf"], linewidth = 1)
    sns.despine()