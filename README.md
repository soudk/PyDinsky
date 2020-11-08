# PyDinsky
PyDinsky team repository for McGill Physics Hackathon 2020

## Why Pydinski
We're creating generative art with user input and elements of randomness. Our name is a play on [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), a Russian painter who pioneered abstract art and used bold colors liberally in his work.

## The "Physics"
Every time you generate an image it will be different. We implemented random walk methods that follow a **Boltzmann distribution** and are seeded with a temperature from a given city. We plot the trace of walkers using a color scheme that matches the given temperature.

## Use your favorite cities to generate images
The color schemes used for the walkers are generated using the current temperature of the cities of your choice, pulled from the [OpenWeather](https://openweathermap.org/) API. A cold scheme for a colder day and a warm scheme for a blazing hot day.

Web app available at: https://pydinsky.herokuapp.com/main-bokeh

Welcome to the paartyyy

![](animation1.gif)![party time](https://github.com/soudk/PyDinsky/blob/main/data/animation1.gif?raw=true)


