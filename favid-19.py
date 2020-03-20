import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mycsv #add location to your csv

df_conf = pd.read_csv(mycsv.confirmed)

print(df_conf)

# Filter for Italy
df_conf = df_conf[df_conf['Country/Region'] == 'Italy']

df_conf.set_index( 'Country/Region' , inplace = True)
df_conf = df_conf.drop(['Lat','Long','Province/State'], axis=1)


df_conf_trans = df_conf.T

#df_conf
df_conf_trans.plot()
plt.show()

def load_csv(csv):
    return pd.csv_read(csv)

def Favid19():
    load_csv('/home/filax/git/COVID-19/')

if( __name__ == '__main__' ):
    #Favid19()
    pass
