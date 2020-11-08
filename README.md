# PyDinsky
PyDinsky team repository for McGill Physics Hackathon 2020

<<<<<<< HEAD
Web app available at: https://pydinsky.herokuapp.com/main-bokeh

=======
>>>>>>> 03d25d17978984022d7a77e3ff568ecf0b1c81c2
## Why Pydinsky
We're creating generative art with user input and elements of randomness. Our name is a play on [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), a Russian painter who pioneered abstract art and used bold colors liberally in his work. Prior to Kandinsky's contributions to mainstream aesthetic theories, what we now call abstract art was rejected as a true art form. To this day, there is a stigma around abstract art. 

<p align="center">
  <img width="460" height="300" src="https://github.com/soudk/PyDinsky/blob/main/data/kadinsky.jpg">
</p>

"What's up with that painting?", you might have heard, or "My three-year-old nephew could have painted this rubbish." This perspective misses a key aspect of art: what emotions do you feel when looking at a piece? Kandinsky argued that abstract art could be equally emotionally impactful as more representative works. He drew comparisons to other art forms, such as music, to argue that simple colors arranged in non-representative ways could move the viewer. Fortunately, paradigm shift has promoted the creation of abstract pieces all over the world, in a diverse and inclusive way. PyDinsky is our modest attempt to be part of this movement and hopefully, you, the viewer, will be moved by what you see here. 

## The Concept
Heat diffusion is familiar to all: temperature fluctuations and movement are part of our everyday experience. Random walks are inherently linked to temperature and diffusion, but are **not** a concept trivially known to all. Our project aims to artistically represent these random walks, using the earth as a stage. The random walk trajectories are based on the live local temperatures in different cities worldwide.

## The "Physics"
The Physics of our project is based around the velocity for a given temperature following Boltzmann distribution. Every image you generate will be different because we implement random walk methods that follow this **Boltzmann distribution** and are seeded with actual temperature from a given city.

<p align="center">
  <img width="460" height="300" src="https://github.com/soudk/PyDinsky/blob/main/data/distribution.png">
</p>

Random variables are sampled from this distribution, with the step size at each iteration depending on the temperature of the city. 

<p align="center">
  <img width="460" height="400" src="https://github.com/soudk/PyDinsky/blob/main/data/temp_map.png">
</p>

Additionally, we implement a routine to approximately extrapolate temperatures over the entire x-y range to obtain temperature at each position on the walk and use this to modify the distribution during run. We then plot the trace of the walkers using a custom-designed color scheme that accords with the given temperature ranges.

## Use Your Favorite Cities to Generate Images
The color schemes used for the walkers are generated using the current temperature of the cities of your choice, pulled from the [OpenWeather](https://openweathermap.org/) API. A cold scheme for a colder day, a warm scheme for a blazing hot day, and a medium scheme for everything in between.

we used the [Bokeh](https://bokeh.org/) python package to generate an interactive web app. You can pick from a list of cities and the weather API is queried for the current temperature. The website is the deployed using [Heroku](https://dashboard.heroku.com/). You can now add as many cities as you like!

On average walkers from hotter cities are more likely to spread out over a wider area due to the wider Boltzmann distribution of velocities. The cities longitude and latitude are projected onto the X-Y plane, and this is where the walker begins. Walkers that hit the boundary walls are reflected to allow for a densely populated figure. 

You can choose which cities to display, and we will query their live temperature as the seed for the art. Click on the legend to show/hide cities and build your art. Each plot generated is unique to your mouse clicks, subject to the current global weather patterns. Have fun!   

## Try It Out
Web app available at: https://pydinsky.herokuapp.com/main-bokeh

[](example_webapp.png)![Exmaple of web app functionality](https://github.com/soudk/PyDinsky/blob/main/data/example_webapp.png?raw=true)

Welcome to the party!

![](animation1.gif)![party time](https://github.com/soudk/PyDinsky/blob/main/data/animation1.gif?raw=true)


