#https://www.kaggle.com/rosado/history-of-tsunamis-1 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style
import sys

tsunami_data = pd.read_csv('sources_clean.csv')

tsunami_data.PRIMARY_MAGNITUDE[tsunami_data.VALIDITY ==4 ].groupby(tsunami_data.PRIMARY_MAGNITUDE).value_counts().plot(kind='bar',
                                             legend=False,
                                             figsize=(11,6),
                                             title= "Primary Magnitudes of tsunamis with a validity >4",
                                             fontsize=6
                                            );
magnitude_median = tsunami_data.PRIMARY_MAGNITUDE.median()
magnitude_mean = tsunami_data.PRIMARY_MAGNITUDE.mean()
#plt.xticks(rotation='horizontal')
print("Median Magnitude of all earthquake related tsunami's:")
print(magnitude_median)
print("Mean Magnitude of all earthquake related tsunami's:")
print(magnitude_mean)
plt.xlabel("PRIMARY_MAGNITUDE")
plt.show()