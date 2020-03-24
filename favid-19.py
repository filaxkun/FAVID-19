import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mycsv #add location to your csv

if ( len(sys.argv) < 2 ):
    print('python3 favid.py <COUNTRY> <INFO>')
    print(' <COUNTRY> : Italy, France, ...h')
    print(' <INFO>    : conf / recov / death')
    exit()

df_list = []

try:
    info = sys.argv[2]
    if ( info == 'conf' or info == 'confirmed' ):
        df_conf = pd.read_csv(mycsv.confirmed)
        df_list.append( df_conf )
    elif ( info == 'recov' or info == 'recovered' ):
        df_recov = pd.read_csv(mycsv.recovered)
        df_list.append( df_recov )
    elif ( info == 'death' ):
        df_deaths = pd.read_csv(mycsv.deaths)
        df_list.append( df_deaths )
except:
    print('No INFO, printing everything (conf, recov, deaths)')
    df_conf   = pd.read_csv(mycsv.confirmed)
    df_recov  = pd.read_csv(mycsv.recovered)
    df_deaths = pd.read_csv(mycsv.deaths)
    df_list   = [ df_conf, df_recov, df_deaths ]

plt.figure()

# Filter for Country
for df in df_list:
    try:
        country = sys.argv[1]
    except:
        country = 'Italy'

    df = df[df['Country/Region'] == country]
    # Manipulation to get mono-row DF
    df.set_index( 'Country/Region', inplace=True )
    df.drop(['Lat','Long','Province/State'], axis=1, inplace=True )
    print( df )
    # Plotting
    plt.plot( df.T['Italy'] )

plt.show()

def load_csv(csv):
    return pd.csv_read(csv)

def Favid19():
    load_csv('/home/filax/git/COVID-19/')

if( __name__ == '__main__' ):
    #Favid19()
    pass
