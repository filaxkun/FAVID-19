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
        df_conf   = ( pd.read_csv(mycsv.confirmed), 'Confirmed' )
        df_list.append( df_conf )
    elif ( info == 'recov' or info == 'recovered' ):
        df_recov  = ( pd.read_csv(mycsv.recovered), 'Recovered' )
        df_list.append( df_recov )
    elif ( info == 'death' ):
        df_deaths = ( pd.read_csv(mycsv.deaths)   , 'Deaths'    )
        df_list.append( df_deaths )
except:
    print('No INFO, printing everything (conf, recov, deaths)')
    # df = [ pd.DF, label ]
    df_conf   = ( pd.read_csv(mycsv.confirmed), 'Confirmed' )
    df_recov  = ( pd.read_csv(mycsv.recovered), 'Recovered' )
    df_deaths = ( pd.read_csv(mycsv.deaths)   , 'Deaths'    )
    df_list   = [ df_conf, df_recov, df_deaths ]

plt.figure()
labels = []

# Filter for Country
for item in df_list:
    try:
        country = sys.argv[1]
    except:
        country = 'Italy'

    item_df    = item[0]
    item_label = item[1]
    # Manipulation to get mono-row DF
    print(item)
    df = item_df[item_df['Country/Region'] == country]
    df.set_index( 'Country/Region', inplace=True )
    #df.drop(['Lat','Long','Province/State'], axis=1, inplace=True )
    df = df.drop(['Lat','Long','Province/State'], axis=1)
    print( item_label, df )
    # Plotting
    #plt.bar( x = df.T.index, height = df.T[country] )
    plt.plot( df.T[country] )
    labels.append( item_label )


plt.legend( labels )
plt.show()

def load_csv(csv):
    return pd.csv_read(csv)

def Favid19():
    load_csv('/home/filax/git/COVID-19/')

if( __name__ == '__main__' ):
    #Favid19()
    pass
