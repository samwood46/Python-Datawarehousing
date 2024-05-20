#https://www.kaggle.com/rosado/history-of-tsunamis-1 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style
import sys

tsunami_data = pd.read_csv('sources_clean.csv')

tsunami_data['YEAR_FREQUENCY'] = tsunami_data.groupby(tsunami_data.YEAR)['YEAR'].transform('count')
tsunami_data.YEAR[tsunami_data.YEAR_FREQUENCY > 50].value_counts().plot(kind='bar',
                                             legend=False,
                                             figsize=(11,6),
                                             title="Tsunamis frequency by continents",
                                             fontsize=10,
                                             alpha=0.5
                                            );
plt.show()