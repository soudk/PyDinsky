# PyDinsky
PyDinsky team repository for McGill Physics Hackathon 2020

## Why Pydinski
We're creating generative art with user input and elements of randomness. Our name is a play on [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), a Russian painter who pioneered abstract art and used bold colors liberally in his work.

## The "Physics"
The Physics that out project includes is based around the velocity for a given temperature following Boltzmann distribution. Every time you generate an image it will be different because we implement random walk methods that follow this **Boltzmann distribution** and are seeded with actual temperature from a given city. 
![alt text](https://github.com/soudk/PyDinsky/blob/main/distribution.png)
Random variables are sampled from this distribution that depends on the temperature of the region to define the step size at each iteration. In addition to this, we also implement a routine to approxiamtely extrapolate temperatures over the entire x-y range to obtain temperature for each position to modify the distribution during run.
We then plot the trace of walkers using a color scheme that matches the given temperature.

## Use your favorite cities to generate images
The color schemes used for the walkers are generated using the current temperature of the cities of your choice, pulled from the [OpenWeather](https://openweathermap.org/) API. A cold scheme for a colder day and a warm scheme for a blazing hot day.

Web app available at: https://pydinsky.herokuapp.com/main-bokeh

Welcome to the paartyyy

![](animation1.gif)![party time](https://github.com/soudk/PyDinsky/blob/main/data/animation1.gif?raw=true)


