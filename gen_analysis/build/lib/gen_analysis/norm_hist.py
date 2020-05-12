import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def hist(ref, test, nbins, label_ref, label_test):
    """This function will return normalized histograms for a specific gene and the ratio of cells that
    shows specific expression levels
    
    Parameters
    ----------
    ref = array
    test = array
    nbins = integer
    label_ref = string
    label_test = string"""
    
    maxref, maxtest = np.max(ref), np.max(test)
    max_ = max(maxref,maxtest)

    bref, beref = np.histogram(ref, bins=nbins, range=(0,max_))
    btest, betest = np.histogram(test, bins=nbins, range=(0,max_))
    bref = bref/len(ref)
    btest = btest/len(test)

    width = beref[-1]/nbins
    plt.bar(beref[:-1], bref, label=label_ref, alpha=.3, width=width)
    plt.bar(beref[:-1], btest, label=label_test, alpha=0.3, width=width)
    plt.legend()
    plt.xlabel('Normalized counts')
    plt.ylabel('Percentage of cells in subpopulation')
    plt.title('')
    sns.despine()