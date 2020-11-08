# PyDinsky
PyDinsky team repository for McGill Physics Hackathon 2020

## Why Pydinski
We're creating generative art with user input and elements of randomness. Our name is a play on [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), a Russian painter who pioneered abstract art and used bold colors liberally in his work. Prior to Kandinsky's contributions to mainstream aesthetic theories, humanity endured a long journey in which it, for multiple centuries, rejected what we would now call abstract art. Still to this day, there is a stigma around abstract art. "What is up with that painting?", you might have heard, "My three years old nephew could have painted this rubbish." This kind of perspective is not focusing on the important matter, being: what emotions do you feel when looking at a piece? Kandinsky contributed a rationale in which he detailed that abstract art could be "digested" emotionally on the same footing as more representative works. He drew comparisons from other art forms, such as music, to show that simple colors arranged in non-representative ways could move the viewer. Fortunatly enough, this change in paradigm has promoted the creation of abstract pieces all over the world, in a diverse and inclusive way. We have now modestly attempted to be part of this movement and hopefully, you, the viewer, will be pleased by what you see here. 

## The Concept
The phenomena of heat diffusion is somewhat familiar to all. Indeed temperature fluctuations and "movement" is part of our everyday experience. A phenomena inheretly linked to temperature and diffusion is that of random walks. This is NOT a concept trivially known to all. With our project, we chose to represent artistically those aforementioned random walks on the stage of the earth. Their trajectories are based on the live local temperatures at different cities in the world. 

## The "Physics"
The Physics that out project includes is based around the velocity for a given temperature following Boltzmann distribution. Every time you generate an image it will be different because we implement random walk methods that follow this **Boltzmann distribution** and are seeded with actual temperature from a given city.

![alt text](https://github.com/soudk/PyDinsky/blob/main/distribution.png)

Random variables are sampled from this distribution that depends on the temperature of the region to define the step size at each iteration. In addition to this, we also implement a routine to approxiamtely extrapolate temperatures over the entire x-y range to obtain temperature for each position to modify the distribution during run.
![alt text](https://github.com/soudk/PyDinsky/blob/main/temp_map.png)

We then plot the trace of walkers using a custom designed color scheme that matches the given temperature ranges.

## Use your favorite cities to generate images
The color schemes used for the walkers are generated using the current temperature of the cities of your choice, pulled from the [OpenWeather](https://openweathermap.org/) API. A cold scheme for a colder day and a warm scheme for a blazing hot day.

Web app available at: https://pydinsky.herokuapp.com/main-bokeh

Welcome to the paartyyy

![](animation1.gif)![party time](https://github.com/soudk/PyDinsky/blob/main/data/animation1.gif?raw=true)


