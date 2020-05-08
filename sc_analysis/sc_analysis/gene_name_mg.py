import mygene as mg
import pandas as pd

def gene_name_mg(x, species):
    
    """A function to convert transcript IDs to gene names using mygene.
     Depending on the species, it will focus the search.
     
     Parameters
     ----------
     x = transcript IDs without version
     species = mouse, human, etc"""
    
    mg = mygene.MyGeneInfo()
    
    list_of_genes = []
    
    if species == "mouse":
        for i in x:
            genes = mg.query(i, fields='symbol', species = "mouse")
            list_of_genes.append(genes["hits"][0]["symbol"])
        return pd.DataFrame(list_of_genes)  
    
    if species == "human":
        for i in x:
            genes = mg.query(i, fields='symbol', species = "human")
            list_of_genes.append(genes["hits"][0]["symbol"])
        return pd.DataFrame(list_of_genes) 