import pandas as pd

def gene_sym_dict(x, dictionary):
    """A function to return a list of gene symbols from a supplied dictionary
    
    Parameters
    ----------
    x = text file or csv of transcript IDs
    dictionary = pandas dataframe of gene names and Gene IDs.
    Make sure the column names are [Gene name] and [Gene stable ID]"""
    
    list_of_genes = []
    
    supplied_dict = pd.Series(dictionary["Gene name"].values,
                              index = dictionary["Gene stable ID"]).to_dict()
  
    for i in x:
        try:
            gene_names = supplied_dict[i]
            list_of_genes.append(gene_names)
        except:
            list_of_genes.append(i)
   
    return pd.DataFrame(list_of_genes)
