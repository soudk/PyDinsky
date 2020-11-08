from bokeh.plotting import figure, curdoc, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select, CustomJS, Rect
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

cities=["none"]
countries=["none"]
coords=["none"]

#What data do we want
for d in data:
        cities.append(d["name"])
        countries.append(d["country"])
        coords.append(d["coord"])

def lon_lat(data):
    x = data[0]
    x = x + 180 # offset of 10
    x = 100*x/(360) # 80 gives an additional padding of 10 on the right
    y = data[1]
    y = y + 90 # offset of 10
    y = 100*y/(180) # 80 gives an additional padding of 10 on the right
    data1 = np.asarray([x,y])
    return [data1]


#INITIAL PLOT - ALWAYS MONTREAL
#WALKERS
CityName = "Montreal"
Country = "Canada"
T = [gt.get_temperature(CityName, Country)]
positions =[[29.6, 75.2]] #Montreal - hard coded, because of the accent screwing things up.
#positions = lon_lat(countries[coords.index(CityName)]) #Montreal - hard coded
#for i in range(num_walkers):
#        positions.append([int(np.random.rand()*100),int(np.random.rand()*100)])
positions = np.asanyarray(positions)
x,y,v,tmap = rw.rand_walker_data(n_grid,T,num_steps,num_walkers,positions)


today = date.today()
date = today.strftime("%B %d, %Y")

#PLOTTING
T_cel = round(T[0]-273.15, 1) #temperature in celsius for use in legends etc...
plot = figure(title = "A Random Walk: "+CityName+", "+ Country +" on "+ date +" , "+str(T_cel)+" "+chr(176)+"C", x_axis_label = "X Position", y_axis_label = "Y Position")
size = 10
color_list = cm.color_assign(v[:,0], cm.FindPalette(T[0]))
plot.line(x[:,0], y[:,0], color = 'grey', line_alpha = 0.2) #colour here should be the average colour
plot.circle(0, 0, size=0.00000001, color= "#ffffff", legend="Cities & Temperatures") #for the legend title
plot.scatter(x[:,0], y[:,0], size=size, color=color_list, fill_alpha = 0.3, legend_label=CityName+": "+str(T_cel)+chr(176)+"C")
plot.legend.click_policy="hide"

# HANDLE BOKEH CALLBACKS ... 

def update_city1(attr, old, new):
    #after an update to the city list
    CityName = dropdown_1.value
    Country = countries[cities.index(CityName)]
    T = [gt.get_temperature(CityName, Country)]
    T_cel = round(T[0]-273.15, 1)
    
    #print("Temperature: ", T[0])  #testing

    tit = "A Random Walk: "+CityName+", "+ Country +" on "+ date +", "+str(round(T[0]-273.15, 1))+" "+chr(176)+"C"
    plot.title.text = tit
    
    #print("------------------------------------", coords[cities.index(CityName)])
    positions = lon_lat([coords[cities.index(CityName)]['lon'], coords[cities.index(CityName)]['lat']])
    positions = positions
    print(positions)
    #for i in range(num_walkers):
    #    positions.append([int(np.random.rand()*100),int(np.random.rand()*100)])
    positions = np.asanyarray(positions)
    x,y,v,tmap = rw.rand_walker_data(n_grid,T,num_steps,num_walkers,positions)
    
    color_list = cm.color_assign(v[:,0], cm.FindPalette(T[0])) #from cm
    #print(color_list)

    plot.line(x[:,0], y[:,0], color = 'grey', line_alpha = 0.2)
    
    #Bokeh scatter plot - look into color argument
    plot.scatter(x[:,0], y[:,0], size=size, color=color_list, fill_alpha = 0.7, legend_label=CityName+": "+str(T_cel)+chr(176)+"C")

    return 0


# CREATE DROPDOWN WIDGET
dropdown_1 = Select(title = "add city to plot", options = cities, value = None)
dropdown_1.on_change('value', update_city1)


# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(dropdown_1, plot))

