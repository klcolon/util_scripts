# Data-Analysis
This repository contains packages for basic statistics and processing tools for biological data.
To install packages, go to the gen_analysis folder and `pip install -e .`.

# Available Modules 
- bootstrap
  -This module is able to generate bootstrap samples, bootstrap replicates, and obtain confidence intervals.
- cohens_d
  -This module calculates cohen's d effect size.
- dkw
  -This module calculates the Dvoretzky–Kiefer–Wolfowitz inequality for ecdfs.
- ecdf
  -This module can generate ecdfs using matplotlib or return ecdf values for a given dataset. Additionally, arguments are        availible to enable point-wise confidence intervals by bootstrapping.
- jaccard_index
  -This module will return the jaccard similarity score. Useful for comparing transcriptome or proteome datasets.
- l1_norm
  -This module will calculates the l1 norm for each gene and is primarily used for differential analysis of single-cell          transcriptomic data. 
- norm_hist
  -This is to generate normalized histograms of genes from single-cell transcriptomic data. This function is used in the l1      norm calculation.
- permutation_mean
  -This module can perform permutation tests comparing the mean. 
- intersect
  -This module can find distinct sets between all possible sample combinations. This function will output a pandas dataframe containing samples being compared, list of unique matches within the compared groups, and the total number of unique elements. Additionally, upset plots can be generated and the corresponding data structure used to generate the plot will also be outputted.
  
 # Documentation
 ```
 class gen_analysis.bootstrap.draw_sample(data)
 
 Parameters
 ----------
 data = 1D array
 ```
 ```
 class gen_analysis.bootstrap.draw_reps(data, test_statistic = "mean", size=1)
 
Parameters
----------
data = 1D dataset
test_statistic = median or mean
size = integer
 ``` 
  ```
gen_analysis.cohens_d(x,y)
 
Parameters
----------
x = array
y = array
 ``` 
```
gen_analysis.dkw_conf_int(x, data, alpha)
 
Parameters
----------
x = array or int or float
data = data used to generate ecdf
alpha = confidence interval
 ``` 
 ```
class gen_analysis.ecdf.values(data, label)
 
Parameters
----------
data = 1D array
label = string
 ``` 
 ```
class gen_analysis.ecdf.plot(data, label_column, val_column, conf = False, color = None)
 
Parameters
----------
data = tidy data with values in one column and labels in another
label_column = column name with categories
value_column = column name with values
color = list
conf = bool
 ``` 
 
