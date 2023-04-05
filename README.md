# Utility Scripts for Biological Data
This repository various utility scripts for basic statistics and processing for biological data. 
To install the package, run the following `pip install .`.

## Dependencies
- numpy == 1.19.0
- pandas == 1.0.1
- matplotlib == 3.1.3
- seaborn == 0.10.0
- upsetplot == 0.4.0
- more-itertools == 8.2.0

## Available Modules 
### bootstrap
- This module is able to generate bootstrap samples, bootstrap replicates, and obtain confidence intervals.
### cohens_d
- This module calculates cohen's d effect size.
### dkw
- This module calculates the Dvoretzky–Kiefer–Wolfowitz inequality for ecdfs.
### ecdf
- This module can generate ecdfs using matplotlib or return ecdf values for a given dataset. Additionally, arguments are        availible to enable point-wise confidence intervals by bootstrapping.
### jaccard_index
- This module will return the jaccard similarity score. Useful for comparing transcriptome or proteome datasets.
### l1_norm
- This module will calculates the l1 norm for each gene and is primarily used for differential analysis of single-cell          transcriptomic data. 
### norm_hist
- This is to generate normalized histograms of genes from single-cell transcriptomic data. This function is used in the l1      norm calculation.
### permutation_mean
- This module can perform permutation tests comparing the mean. 
### intersect
- This module can find distinct sets between all possible sample combinations. This function will output a pandas dataframe containing samples being compared, list of unique matches within the compared groups, and the total number of unique elements. Additionally, upset plots can be generated and the corresponding data structure used to generate the plot will also be outputted.
