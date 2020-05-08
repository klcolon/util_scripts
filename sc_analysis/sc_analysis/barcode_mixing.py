import pandas as pd

def barcode_mixing(dataframe, threshold, number_of_tags):
 
    '''This function is to identify cells that have mixed cell barcodes
    
    Parameters
    ----------
    dataframe = gene by cell matrix
    threshold = integer
    number_of_tags = integer'''

    cells_with_extra_tags = []

    if number_of_tags is 2:
        for index, row in dataframe.iterrows():
            if row['CS_SGR1'] > threshold and row['CS_SGR2'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR1'] > threshold and row['CS_SGR3'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR1'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR2'] > threshold and row['CS_SGR3'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR2'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR3'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
    elif number_of_tags is 3:
        for index, row in dataframe.iterrows():
            if row['CS_SGR1'] > threshold and row['CS_SGR2'] > threshold and row['CS_SGR3'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR1'] > threshold and row['CS_SGR2'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR1'] > threshold and row['CS_SGR3'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
            elif row['CS_SGR2'] > threshold and row['CS_SGR3'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)
    elif number_of_tags is 4:  
        for index, row in dataframe.iterrows():
            if row['CS_SGR1'] > threshold and row['CS_SGR2'] > threshold and row['CS_SGR3'] > threshold and row['CS_SGR4'] > threshold:
                cells_with_extra_tags.append(index)

    return (cells_with_extra_tags)