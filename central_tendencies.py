#https://www.kaggle.com/rosado/history-of-tsunamis-1 
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
from matplotlib import style
import sys

tsunami_data = pd.read_csv('sources_clean.csv')

#MODE VALUES OF VALIDITY FOR EACH CONTINENT
tsunami_continent_europe = tsunami_data[tsunami_data['CONTINENT'] == 'EUROPE']
europe_validty_mode = tsunami_continent_europe.VALIDITY.mode()
europe_validty_mean = tsunami_continent_europe.VALIDITY.mean()


tsunami_continent_africa = tsunami_data[tsunami_data['CONTINENT'] == 'AFRICA']
africa_validty_mode = tsunami_continent_africa.VALIDITY.mode()
africa_validty_mean = tsunami_continent_africa.VALIDITY.mean()

tsunami_continent_northamerica = tsunami_data[tsunami_data['CONTINENT'] == 'NORTH_AMERICA']
northamerica_validty_mode = tsunami_continent_northamerica.VALIDITY.mode()
northamerica_validty_mean = tsunami_continent_northamerica.VALIDITY.mean()


tsunami_continent_southamerica = tsunami_data[tsunami_data['CONTINENT'] == 'SOUTH_AMERICA']
southamerica_validty_mode = tsunami_continent_southamerica.VALIDITY.mode()
southamerica_validty_mean = tsunami_continent_southamerica.VALIDITY.mean()


tsunami_continent_asia = tsunami_data[tsunami_data['CONTINENT'] == 'ASIA']
asia_validty_mode = tsunami_continent_asia.VALIDITY.mode()
asia_validty_mean = tsunami_continent_asia.VALIDITY.mean()



tsunami_continent_australia = tsunami_data[tsunami_data['CONTINENT'] == 'AUSTRALIA']
australia_validty_mode = tsunami_continent_australia.VALIDITY.mode()
australia_validty_mean = tsunami_continent_australia.VALIDITY.mean()


tsunami_continent_antarctica = tsunami_data[tsunami_data['CONTINENT'] == 'ANTARCTICA']
antarctica_validty_mode = tsunami_continent_antarctica.VALIDITY.mode()
antarctica_validty_mean = tsunami_continent_antarctica.VALIDITY.mean()



#validity modes
print("europe validty mode: ")
print(europe_validty_mode)
print(" ")
print("africa validty mode: ")
print(africa_validty_mode)
print(" ")
print("north america validty mode: ")
print(northamerica_validty_mode)
print(" ")
print("south america validty mode: ")
print(southamerica_validty_mode)
print(" ")
print("asia validty mode: ")
print(asia_validty_mode)
print(" ")
print("antarctica validty mode: ")
print(antarctica_validty_mode)
print(" ")

#validity mean per continent 
print("europe validty mean: ")
print(europe_validty_mean)
print(" ")
print("africa validty mean: ")
print(africa_validty_mean)
print(" ")
print("north america validty mean: ")
print(northamerica_validty_mean)
print(" ")
print("south america validty mean: ")
print(southamerica_validty_mean)
print(" ")
print("asia validty mean: ")
print(asia_validty_mean)
print(" ")
print("antarctica validty mean: ")
print(antarctica_validty_mean)
