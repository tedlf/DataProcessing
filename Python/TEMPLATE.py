'''
Template graph generation script. All teh required methods are heavily noted in this file

First note: This file was converted directly from .ipynb. It will generate a lot of verbose comments.
For educational purpaces, I will leave them all in.

'''
# coding: utf-8

# 4915DataProcessing/Scouting_GP.py
# Written in Pyhton 3
# Written by Darwin C 




# Analysis imports
import pandas as pd
import numpy as np
import time
# Graphing imports
import matplotlib.pyplot as plt

# Pretty colors imports
from itertools import cycle, islice

# Matches for the remaining of Portland, as of 4/6 ~ Noon
MATCHES = [[2990,2906,997,3024,4915,4450],
               [4512,1425,4915,3674,6845,3218],
               [6845,4915,2928,3826,4469,3238],
               [4915,2521,6831,847,4450,2944],
               [1318,4512,6445,997,1778,4915],
               [488,1359,1425,3663,4915,6076],
               [4915,2930,2605,3223,4662,2471],
               [2930,2557,5803,4915,4125,847]]

# All matches for days 2 and 3 for portland


''' This is the first required function. This is nessissary because  '''


def import_message():

    return "TEMPLATE.py successfully imported!"

def read_data():

    raw_data = pd.read_csv('Data/Portland_Data.csv',header=3,index_col=3,usecols=range(3,16))

    # Deprecated, but used to turn % numbers into integers
    def remove_percentage(s):
        if isinstance(s, str):
            return float(s.rstrip('%'))
        else:
            return 0


    # In[298]:


    # Createing the table, indexed by team #, with 4 important data points.
    data = raw_data.groupby(['Team #'])['Scale Cubes', 'Switch Cubes', 'Opponent Switch Cubes',
                                  'Exchange Cubes'].mean()

    # SEE THOSE NaN, I DON'T EITHER
    data.fillna(value=0,axis=1,inplace=True)

    # Create another col, which is an addition of all the other cols
    data['Total Cubes'] = data['Scale Cubes'] + data['Switch Cubes']     + data['Opponent Switch Cubes'] + data['Exchange Cubes']

    # Sort by the maximum number of cubes
    data = data.sort_values(by='Total Cubes', ascending=False)

    return data
   # In[291]:




# In[292]:
''' This is not a required function, This will most likely end up being a debug function '''
def show_data(data):
    data.head()
    data.describe()



'''
# Stacked table
plot1 = data[['Scale Cubes', 'Switch Cubes', 'Opponent Switch Cubes',
              'Exchange Cubes']].plot(kind='bar', stacked=True, title='Tele Cubes',figsize=(18.5, 10.5))

plot1.set_xlabel('Team')
plot1.set_ylabel('Total cubes');




# Individual table
plot2 = data['Scale Cubes'].plot(kind='bar', stacked=True, title='Scale Cubes', color='green')
plot2.set_xlabel('Team')
plot2.set_ylabel('Avg Scale');



# Individual table
plot3 = data['Switch Cubes'].plot(kind='bar', stacked=True, title='Own Switch Cubes', color='blue')
plot3.set_xlabel('Team')
plot3.set_ylabel('Avg Own Switch');




# First test of a larger table
plot4 = data['Opponent Switch Cubes'].plot(kind='bar', stacked=True, title='Opp Switch Cubes', color='red',grid=True,figsize=(18.5, 10.5))
plot4.set_xlabel('Team')
plot4.set_ylabel('Avg Opp Switch');



# Experementing with color slices in a stacked bar chart.
my_colors  = [(x/10.0, x/20.0, 0.75) for x in range(len(data))] # <-- Quick gradient example along the Red/Green dimensions.

plot5 = (data.loc[[4915,360,488]].plot(kind='bar',colormap='Paired',figsize=(18.5,10.5),grid=True,stacked=True))
'''



# pump out graphs for days 2 and 3
# Used to label the graph
def gen_graphs(data):

    match = [2990,2906,997,3024,4915,4450] 

    # generating the graph
    graph = data.loc[match].plot(kind='bar',title="Spartronics 4915 1st match of the day!",figsize=(18.5,10.5),grid=True,colormap='winter')
        
    graph.set_ylabel('Cubes Manipulated');

    fig = graph.get_figure()

    # List of names of output graphs 
    export = []

    # NOTE: This is a potental location of a for loop.
    # If you want to save multiple graphs, then it would be someting like
    '''
    
    for match in MATCHES:
        matchcount += 1

        graph = data.loc[match].plot(kind='bar',title="Spartronics 4915 " + str(matchcount) + "st match of the day!",figsize=(18.5,10.5),grid=True,colormap='winter')
        
        graph.set_ylabel('Cubes Manipulated');
fig = graph.get_figure()


    '''
    # The critical part is that 'export' is appended, because if it is not it will cause problems in compute.py

    fig.savefig("TEMPLATE Graph")


    # Support for multiple files
    export.append("TEMPLATE Graph.png")
   
    return export
