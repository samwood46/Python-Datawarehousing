#https://www.kaggle.com/rosado/history-of-tsunamis-1 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style
import sys

tsunami_data = pd.read_csv('sources_clean.csv')
'''
#Mapping different causes
causes = {0:'Unknown',
          1:'Earthquake',
          2:'Questionable Earthquake',
          3:'Earthquake and Landslide',
          4:'Volcano and Earthquake',
          5:'Volcano, Earthquake, and Landslide',
          6:'Volcano',
          7:'Volcano and Landslide',
          8:'Landslide',
          9:'Meteorological',
          10:'Explosion',
          11:'Astronomical Tide'}

tsunami_data['CAUSE'] = tsunami_data['CAUSE'].map(causes)

#Group by Causes 
tsunami_data['CAUSES_FREQUENCY'] = tsunami_data.groupby(tsunami_data.CAUSE)['CAUSE'].transform('count')

#Causes of tsunamis Figure 3
tsunami_data.CAUSE[tsunami_data.CAUSES_FREQUENCY >= 50].value_counts().plot(kind='pie',
                                            legend=False,
                                            figsize=(13,13),
                                            title="Causes of tsunamis, Figure 3",
                                            autopct='%.1f%%');

'''
#Group by Continent
tsunami_data['CONTINENT_FREQUENCY'] = tsunami_data.groupby(tsunami_data.CONTINENT)['CONTINENT'].transform('count')

#Figure 10  Frecuency tsunamis by Continent
tsunami_data.CONTINENT[tsunami_data.CONTINENT_FREQUENCY > 1].value_counts().plot(kind='bar',
                                             legend=False,
                                             figsize=(11,6),
                                             title="Tsunamis frequency by continents",
                                             fontsize=10,
                                             alpha=0.5
                                            );

#Mapping different causes
causes = {0:'Unknown',
          1:'Earthquake',
          2:'Questionable Earthquake',
          3:'Earthquake and Landslide',
          4:'Volcano and Earthquake',
          5:'Volcano, Earthquake, and Landslide',
          6:'Volcano',
          7:'Volcano and Landslide',
          8:'Landslide',
          9:'Meteorological',
          10:'Explosion',
          11:'Astronomical Tide'}

tsunami_data['CAUSE'] = tsunami_data['CAUSE'].map(causes)


tsunami_continent_europe = tsunami_data[tsunami_data['CONTINENT'] == 'EUROPE' and tsunami_data['VALIDITY'] ]  
europe_cause_mode = tsunami_continent_europe.CAUSE.mode()



tsunami_continent_africa = tsunami_data[tsunami_data['CONTINENT'] == 'AFRICA']
africa_cause_mode = tsunami_continent_africa.CAUSE.mode()


tsunami_continent_northamerica = tsunami_data[tsunami_data['CONTINENT'] == 'NORTH_AMERICA']
northamerica_cause_mode = tsunami_continent_northamerica.CAUSE.mode()



tsunami_continent_southamerica = tsunami_data[tsunami_data['CONTINENT'] == 'SOUTH_AMERICA']
southamerica__mode = tsunami_continent_southamerica.CAUSE.mode()



tsunami_continent_asia = tsunami_data[tsunami_data['CONTINENT'] == 'ASIA']
asia_cause_mode = tsunami_continent_asia.CAUSE.mode()




tsunami_continent_australia = tsunami_data[tsunami_data['CONTINENT'] == 'AUSTRALIA']
australia_cause_mode = tsunami_continent_australia.CAUSE.mode()



tsunami_continent_antarctica = tsunami_data[tsunami_data['CONTINENT'] == 'ANTARCTICA']
antarctica_cause_mode = tsunami_continent_antarctica.CAUSE.mode()

print("europe cause mode: ")
print(europe_cause_mode)
print(" ")
print("africa cause mode: ")
print(africa_cause_mode)
print(" ")
print("north america cause mode: ")
print(northamerica_cause_mode)
print(" ")
print("south america cause mode: ")
print(southamerica_cause_mode)
print(" ")
print("asia cause mode: ")
print(asia_cause_mode)
print(" ")
print("australia cause mode: ")
print(australia_cause_mode)
print(" ")
print("antarctica cause mode: ")
print(antarctica_cause_mode)
print(" ")



plt.xticks(rotation='horizontal')
plt.show()