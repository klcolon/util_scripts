import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def hist(ref, test, nbins, label_ref, label_test):
    """This function will return normalized histograms for a specific gene and the ratio of cells that
    shows specific expression levels
    
    Parameters
    ----------
    ref = 1D array
    test = 1D array
    nbins = integer
    label_ref = string
    label_test = string"""
  
    # get max and min values from the two subpopulations
    max1, max2 = np.max(test), np.max(ref)
    min1, min2 = np.min(test), np.min(ref)

    # get max and min value to define histogram range
    max_ = max(max1,max2)
    min_ = min(min1,min2)

    #compute histogram
    hist1, binedge1 = np.histogram(test, bins=nbins, range=(min_,max_))
    hist2, binedge2 = np.histogram(ref, bins=nbins, range=(min_,max_))
    hist1 = hist1/len(test) # fraction of cells
    hist2 = hist2/len(ref) # fraction of cells

    #plot histogram
    width = binedge2[-1]/nbins
    plt.bar(binedge2[:-1], hist2, label=label_ref, alpha=.3, width=width)
    plt.bar(binedge2[:-1], hist1, label=label_test, alpha=0.3, width=width)
    plt.legend()
    plt.xlabel('Normalized counts')
    plt.ylabel('Percentage of cells in subpopulation')
    plt.title('')
    sns.despine()