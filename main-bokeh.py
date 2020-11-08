from bokeh.plotting import figure, curdoc, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.palettes import magma  #actually going to use cutom pallete
import numpy as np
from datetime import date

# GENERATE STARTING GRAPHS

source_cities = ColumnDataSource(data = {
    'x': [0],
    'y': [0]
})


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
select_city.on_change('value', update_city)

"""


CityName = "Montreal" #replace this with input from temperature / dropdown box


today = date.today()

date = today.strftime("%B %d, %Y")

#Plot area 
plot = figure(title = "A Random Walk through "+CityName+" on "+ date, x_axis_label = "X Position", y_axis_label = "Y Position")

#From link:
# color value of the scatter points 
color = magma(256) #here is how we do colour - velocity

#Example data - replace with walker data
x = np.random.randn(1000)
y = np.random.randn(1000)
v = np.random.randn(1000)


# ADD INITIAL PLOT - SEE BOKEH DOCS -- CHANGE THIS
size = 10
plot.line(x, y, color = 'grey', line_alpha = 0.2)
plot.scatter(x, y, size=size, color=color, fill_alpha = 0.7)

# FORMAT/CREATE THE DOCUMENT TO RENDER
curdoc().add_root(column(plot))
