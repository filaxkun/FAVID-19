import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

confirmed = '/home/filax/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
recovered = '/home/filax/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'
deaths = '/home/filax/git/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
who = '/home/filax/git/COVID-19/who_covid_19_situation_reports/who_covid_19_sit_rep_time_series/who_covid_19_sit_rep_time_series.csv'

df_conf = pd.read_csv(confirmed)

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
