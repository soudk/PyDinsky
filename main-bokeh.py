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
    return 0
    #change x, y data values
    #source_zip1.data = {
    #        'x': df_zip1['month'],
    #        'y': df_zip1['hours_elapsed']
    #}

# list of zipcodes to display in dropdown


#TODO: need to pull city names from JSON
with open('data/city_list.json', 'r') as json_file:
    data = json.load(json_file)

cities=[]
#What data do we want
for d in data:
    cities.append(d["name"])

# CREATE DROPDOWN WIDGET
select_city = Select(title = "city", options = cities, value = None)

# ATTACH UPDATE_ZIP1 CALLBACK TO 'VALUE' PROPERTY OF SELECT_ZIP1
select_city.on_change('value', update_city)


CityName = "Montreal" #replace this with input from temperature / dropdown box


today = date.today()

date = today.strftime("%B %d, %Y")

#Plot area 
plot = figure(title = "A Random Walk through "+CityName+" on "+ date, x_axis_label = "X Position", y_axis_label = "Y Position")

#WALKERS
num_walkers = 1
num_steps = 1000
n_grid = num_steps*10
T = np.linspace(100,1000,num_walkers) # Temperature
x,y,v = rw.rand_walker_data(n_grid,T,num_steps,num_walkers)

cities = ["Toronto"]
country= ["Canada"]
temperatures=[]
for i, city in enumerate(cities): 
    temperatures.append(gt.get_temperature(city, country[i]))

##


######################################################

#INITIAL PLOT - ALWAYS MONTREAL
#WALKERS
num_walkers = 1
num_steps = 1000
n_grid = num_steps*10
T = [gt.get_temperature("Montreal", "Canada")]
x,y,v = rw.rand_walker_data(n_grid,T,num_steps,1)

plot.line(x, y, color = 'grey', line_alpha = 0.2) #colour here should be the average colour
plot.scatter(x, y, size=size, color=magma(256), fill_alpha = 0.7)


#after an update to the city list
#for i in range(len(cities)):
#    #color_list = cm.color_assign(v[:,i], cm.FindPalette(5, 15, temperatures[i])) #from cm
#    plot.line(x[:,i], y[:,i], color = 'grey', line_alpha = 0.2)
#    plot.scatter(x[:,i], y[:,i], size=size, color=magma(256), fill_alpha = 0.7)

# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(plot, select_city, select_city))
