from bokeh.plotting import figure, curdoc, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import magma  #actually going to use cutom pallete
import random #nto needed once random walker is working
import numpy as np

# Import walker data here

# GENERATE STARTING GRAPHS

source_cities = ColumnDataSource(data = {
    'x': [0],
    'y': [0]
})

#Plot area 
plot = figure(title = "Random Walk", x_axis_label = "X Position", y_axis_label = "Y Position")

#From link:
# color value of the scatter points 
color = magma(256) #here is how we do colour - velocity

#Example data
x = np.random.randn(1000)
y = np.random.randn(1000)
v = np.random.randn(1000)


# ADD INITIAL PLOT - SEE BOKEH DOCS -- CHANGE THIS
size = 1
plot.line(x, y, color = 'grey')
plot.scatter(x, y, size=size, color=color)

#plot.line('x', 'y', source = source_zip1, line_color = "blue", legend_label = "Zipcode 1")


"""
# HANDLE CALLBACKS ... user choice of incident_zip from dropdown

def update_city(attr, old, new):
    #df_zip1 = df_month[df_month['incident_zip'] == float(select_zip1.value)] #data filtering -- unused if one city
    
    #change x, y data values
    source_zip1.data = {
            'x': df_zip1['month'],
            'y': df_zip1['hours_elapsed']
    }

# list of zipcodes to display in dropdown

#cities = df_month.incident_zip.unique().tolist() #need to pull city names from JSON
#string_cities = [str(zipcode) for zipcode in zipcodes] #string casting

# CREATE DROPDOWN WIDGET
select_city = Select(title = "city", options = string_cities, value = None)

# ATTACH UPDATE_ZIP1 CALLBACK TO 'VALUE' PROPERTY OF SELECT_ZIP1
select_cities.on_change('value', update_city)

"""

# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(select_zip1, select_zip2, plot))
