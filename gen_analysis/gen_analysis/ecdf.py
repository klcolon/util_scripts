import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ecdf:    
    def values(data, label):
        """Calculates ecdf from a 1D array

        Parameters
        ----------
        data = 1D array
        label = string

        Returns 
        Pandas dataframe with ecdf values, labels, and x values
        """

        data = data[~np.isnan(data)]
        ecdf = pd.DataFrame(np.arange(1, len(data)+1) / len(data))
        ecdf['Label'] = label
        ecdf['Values'] = np.sort(data)
        ecdf.columns = ["ecdf", "Label", "Values"]

        return ecdf

    def plot(data, label_column, val_column, color = None):
        """generates ecdf plots

        Parameters
        ----------
        data = tidy data with values in one column and labels in another
        label_column = column name with categories
        value_column = column name with values
        color = list

        Returns 
        ecdf plot using matplotlib
        """

        #obtain unique values
        labels = data[label_column].unique()

        #calculate ecdf for every label
        ecdf_list = []
        for i in labels:
            sliced_data = data.loc[data[label_column] == i]
            ecdf_val = ecdf.values(sliced_data[val_column].values, i)
            ecdf_list.append(ecdf_val)

        #plot
        for i in range(len(ecdf_list)):
            plt.step(ecdf_list[i]["Values"], ecdf_list[i]["ecdf"], linewidth = 2, 
                     label = ecdf_list[i]["Label"][0], color = color[i])
        plt.legend()
        sns.despine()

            