import numpy as np
import pandas as pd

class l1norm_genes:
    
    def l1norm_single(arr1, arr2, nbins):
        '''
        Compute the l1-norm between two histograms

        Parameters
        ----------
        arr1 : sparse matrix
            Matrix of first subpopulation
        arr2 : sparse matrix
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

    def l1_norm_all(test, control, nbins):

        """Calculate the l1 norm between histograms and output the l1_norm list. Make sure
        that the data matrix is gene x cell.

        Parameters
        ----------
        test = array or matrix
        control = array or matrix
        nbins = int
        """ 
        #calculate historgams
        #log transform entire data
        treatment = np.log1p(test)
        control = np.log1p(control)

        l1_norm_list = []

        for gene in range(test.shape[0]):
            # get max and min values from the two subpopulations
            max1, max2 = np.max(treatment[gene,:]), np.max(control[gene,:]) 
            min1, min2 = np.min(treatment[gene,:]), np.min(control[gene,:])

            # get max value to define histogram range
            max_ = max(max1,max2) 
            min_ = min(min1,min2)

            #compute histograms
            if max_ == 0:
                l1_norm_list.append(0) 
            else:
                hist1, binedge1 = np.histogram(treatment[gene,:], bins=20, range=(min_,max_)) 
                hist2, binedge2 = np.histogram(control[gene,:], bins=20, range=(min_,max_)) 
                hist1 = hist1/len(treatment[gene,:]) # fraction of cells
                hist2 = hist2/len(control[gene,:]) # fraction of cells
                l1_norm_list.append(np.linalg.norm(hist1-hist2, ord=1))

        l1_norm = pd.DataFrame(data= l1_norm_list) 

        return l1_norm