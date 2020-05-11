def jaccard_index(list_1, list_2):
    
    """A function to determine the jaccard index between two lists
    Parameters
    ----------
    list_1 = first list
    list_2 = second list
    
    Returns
    -------
    jaccard similarity score"""
    
    match = len(set(list_1).intersection(list_2))
    total_elements = list_1 + list_2
    unique_elements = len(set(total_elements))
    
    return (match/unique_elements)
    
    