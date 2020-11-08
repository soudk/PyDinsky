from bokeh.plotting import figure, curdoc, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import magma  #actually going to use cutom pallete
from bokeh.themes import built_in_themes

import numpy as np
from datetime import date
import json

import sys
sys.path.append('./src/')

import colormap as cm
import random_walker as rw
import get_temperature as gt


# GENERATE STARTING GRAPHS
num_walkers = 1
num_steps = 3000
n_grid = 100


#READ JSON DATA
with open('data/shorter_city_list.json', 'r') as json_file:
    data = json.load(json_file)

cities=[]
countries=[]
coords=[]
#What data do we want
for d in data:
        cities.append(d["name"])
        countries.append(d["country"])
        coords.append(d["coord"])

#print(data[0]) #testing


#INITIAL PLOT - ALWAYS MONTREAL
#WALKERS
CityName = "Montreal"
Country = "Canada"
T = [gt.get_temperature(CityName, Country)]
positions = []
for i in range(num_walkers):
        positions.append([int(np.random.rand()*100),int(np.random.rand()*100)])
positions = np.asanyarray(positions)
x,y,v,tmap = rw.rand_walker_data(n_grid,T,num_steps,num_walkers,positions)


today = date.today()
date = today.strftime("%B %d, %Y")

#PLOTTING
plot = figure(title = "A Random Walk: "+CityName+", "+ Country +" on "+ date +" , "+str(round(T[0]-273.15, 1))+" "+chr(176)+"C", x_axis_label = "X Position", y_axis_label = "Y Position")
size = 10
color_list = cm.color_assign(v[:,0], cm.FindPalette(T[0]))
plot.line(x[:,0], y[:,0], color = 'grey', line_alpha = 0.2) #colour here should be the average colour
plot.scatter(x[:,0], y[:,0], size=size, color=color_list, fill_alpha = 0.3)


# HANDLE BOKEH CALLBACKS ... 

def update_city1(attr, old, new):
    #after an update to the city list
    CityName = dropdown_1.value
    Country = countries[cities.index(CityName)]
    T = [gt.get_temperature(CityName, Country)]
    
    tit = "A Random Walk: "+CityName+", "+ Country +" on "+ date +", "+str(round(T[0]-273.15, 1))+" "+chr(176)+"C"
    plot.title.text = tit
    positions = []
    for i in range(num_walkers):
        positions.append([int(np.random.rand()*100),int(np.random.rand()*100)])
    positions = np.asanyarray(positions)
    x,y,v,tmap = rw.rand_walker_data(n_grid,T,num_steps,num_walkers,positions)
    color_list = cm.color_assign(v[:,0], cm.FindPalette(T[0])) #from cm
    plot.line(x[:,0], y[:,0], color = 'grey', line_alpha = 0.2)
    plot.scatter(x[:,0], y[:,0], size=size, color=color_list, fill_alpha = 0.7)
    return 0


# CREATE DROPDOWN WIDGET
dropdown_1 = Select(title = "city", options = cities, value = None)
dropdown_1.on_change('value', update_city1)


# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(dropdown_1, plot))
