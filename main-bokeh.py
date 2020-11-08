from bokeh.plotting import figure, curdoc, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import magma  #actually going to use cutom pallete
import numpy as np
from datetime import date
import json

import sys
sys.path.append('./src/')

import colormap as cm
import random_walker as rw
import get_temperature as gt

# GENERATE STARTING GRAPHS

source_cities = ColumnDataSource(data = {
    'x': [0],
    'y': [0]
})



# HANDLE CALLBACKS ... user choice of incident_zip from dropdown

def update_city(attr, old, new):
    #after an update to the city list
    #for i in range(len(cities)):
        #color_list = cm.color_assign(v[:,i], cm.FindPalette(5, 15, temperatures[i])) #from cm
        #plot.line(x[:,i], y[:,i], color = 'grey', line_alpha = 0.2)
        #plot.scatter(x[:,i], y[:,i], size=size, color=magma(256), fill_alpha = 0.7)
    #change x, y data values
    #source_zip1.data = {
    #        'x': df_zip1['month'],
    #        'y': df_zip1['hours_elapsed']
    #}
    return 0

# list of zipcodes to display in dropdown


#READ JSON DATA
with open('data/city_list.json', 'r') as json_file:
    data = json.load(json_file)

cities=[]
#What data do we want
for d in data:
    if d["country"]=="Canada":
        cities.append(d["name"])

# CREATE DROPDOWN WIDGET
select_city_1 = Select(title = "city", options = cities, value = None)
select_city_2 = Select(title = "city", options = cities, value = None)
select_city_3 = Select(title = "city", options = cities, value = None)
select_city_4 = Select(title = "city", options = cities, value = None)

select_city_1.on_change('value', update_city)
select_city_2.on_change('value', update_city)
select_city_3.on_change('value', update_city)
select_city_4.on_change('value', update_city)


CityName = "Montreal" #replace this with input from temperature / dropdown box
today = date.today()
date = today.strftime("%B %d, %Y")

#WALKERS
#num_walkers = 1
#num_steps = 1000
#n_grid = num_steps*10
#T = np.linspace(100,1000,num_walkers) # Temperature
#x,y,v = rw.rand_walker_data(n_grid,T,num_steps,num_walkers)

#cities = ["Toronto"]
#country= ["Canada"]
#temperatures=[]
#for i, city in enumerate(cities): 
#    temperatures.append(gt.get_temperature(city, country[i]))


######################################################

#INITIAL PLOT - ALWAYS MONTREAL
#WALKERS
num_walkers = 1
num_steps = 1000
n_grid = num_steps*10
CityName = "Yellowknife"
Country = "Canada"
T = [gt.get_temperature(CityName, Country)]
x,y,v = rw.rand_walker_data(n_grid,T,num_steps,num_walkers)

plot = figure(title = "A Random Walk through "+CityName+", "+ Country +" on "+ date +" , "+str(round(T[0]-273.15, 1))+" "+chr(176)+"C", x_axis_label = "X Position", y_axis_label = "Y Position")

#PLOTTING
size = 10
color_list = cm.color_assign(v[:,0], cm.FindPalette(T[0]))
plot.line(x[:,0], y[:,0], color = 'grey', line_alpha = 0.2) #colour here should be the average colour
plot.scatter(x[:,0], y[:,0], size=size, color=color_list, fill_alpha = 0.7)



# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(select_city_1, select_city_2, select_city_3, select_city_4, plot))
