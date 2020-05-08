import pandas as pd

def remove_version(x):
    '''A funtion to remove version numbers from ensemble IDs'''
    gene_ids = []
    
    for i in x:
        gene_ids.append(i.split(".")) 
    for i in gene_ids:
        del i[1]
        
    flattened_list = []
    
    for j in gene_ids:
        for k in j:
            flattened_list.append(k)
            
    return flattened_list