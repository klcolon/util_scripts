def l1norm(ig, arr1, arr2, nbins):
    '''
    Compute the l1-norm between two histograms

    Parameters
    ----------
    ig : int
        Index of gene
    sub1 : sparse matrix
        Matrix of first subpopulation
    sub2 : sparse matrix
        Matrix of second subpopulation
    nbins : int
        Number of histogram bins to use
    '''
    max1, max2 = np.max(arr1), np.max(arr2) # get max values from the two subpopulations
    max_ = max(max1,max2) # get max value to define histogram range
    if max_ == 0:
        return 0
    else:
        b1, be1 = np.histogram(arr1, bins=nbins, range=(0,max_)) # compute histogram bars
        b2, be2 = np.histogram(arr2, bins=nbins, range=(0,max_)) # compute histogram bars
        b1 = b1/len(arr1) # scale bin values
        b2 = b2/len(arr2) # scale bin values
        if arr1.mean()>=arr2.mean(): # sign l1-norm value based on mean difference
            return -np.linalg.norm(b1-b2, ord=1)
        else:
            return np.linalg.norm(b1-b2, ord=1)