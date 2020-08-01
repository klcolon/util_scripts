import pandas as pd
import numpy as np
from itertools import combinations
from upsetplot import from_memberships
from upsetplot import plot
import matplotlib.pyplot as plt

def intersect(data, upset_plot = False):
    """A function that returns all possible distinct intersections and generates an upset plot
    Parameters
    ----------
    data = pandas dataframe
    upset_plot = boolean
    
    Returns
    -------
    df_final = dataframe with list of matches for each comparison and counts
    upset = data formatted to generate upset plots """

    #isolate column names
    col_names = data.columns.unique()

    #total groups
    n = len(col_names)

    #generate all possible combinations for intersection analysis
    comb_list = []
    for i in range(2,n+1):
        comb_list.append(list(combinations(col_names, i)))

    #find all unique elements and drop na
    unique_elem = []
    tot_elements = []
    for i in col_names:
        unique_elem.append(set(data[i].dropna().to_list()))
    for i in range(len(unique_elem)):
        tot_elements.append([col_names[i], len(unique_elem[i])])
    
    print("Total unique number of items", tot_elements)

    
    #make dictionary for unique elements 
    dict_ = {}
    for i in range(len(col_names)):
        dict_.update({col_names[i]: unique_elem[i]})

    #intersect data, find distinct sets, drop na
    list_intersect = []
    for i in comb_list:
        for j in i:
            if len(j) == 2:
                func_1 = "set(data['{x}'].dropna().to_list()).intersection(data['{y}'].dropna().to_list())".format(x = j[0], y = j[1])
                inter = eval(func_1)
                dict_adj = []
                for i, k in dict_.items():  
                    if i != j[0] and i != j[1]:
                        dict_adj.append(k) 
                for i in dict_adj:
                    unique = inter - i
                    inter = unique
                list_intersect.append([j,list(inter), len(list(inter))])
            else:
                func_2 = "set(data['{x}'].dropna().to_list()).intersection(data['{y}'].dropna().to_list())".format(x = j[0], y = j[1])
                cond = "i != j[0] and i != j[1]"
                for _ in range(2,len(j)):
                    decor_1 = ".intersection(data['{z}'].dropna().to_list())".format(z = j[_])
                    decor_2 = " and i != j[{x}]".format(x = _)
                    func_2 = func_2 + decor_1
                    cond = cond + decor_2
                inter = eval(func_2)
                dict_adj = []
                for i, k in dict_.items():  
                    if eval(cond):
                        dict_adj.append(k) 
                for i in dict_adj:
                    unique = inter - i
                    inter = unique
                list_intersect.append([j,list(inter), len(list(inter))])

    #obtain elements found only in individual datasets
    for j in range(len(col_names)):
        for i in list_intersect:
            if col_names[j] in set(i[0]):
                unique_elem[j] = unique_elem[j] - set(i[1]) 
        unique_elem[j] = list(unique_elem[j])

    #create dataframe for elements found only in individual datasets
    df_1 = pd.DataFrame(col_names)
    df_1[1] = np.array(unique_elem, dtype=object).T
    df_1[2] = [len(i) for i in unique_elem]

    #combine intersect data and unique elements found within individual sets
    df_2 = pd.DataFrame(list_intersect)
    df_3 = pd.concat([df_1,df_2])
    df_3.columns = ["Intersection", "Match", "Counts"]
    df_3 = df_3.reset_index(drop = True)
    
    #generate data structure for upset plot
    upset = df_3.drop("Match", axis=1)
    lst_1 = df_3["Intersection"].to_list()
    lst_2 = df_3["Intersection"].to_list()
    for i in range(len(col_names)):
        lst_1[i] = [lst_2[i]]
    upset = from_memberships(
    lst_1, data=upset["Counts"])
    
    #make upset plot
    if upset_plot == True:
        plot(upset)
    
    return df_3, upset 