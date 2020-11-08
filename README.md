# PyDinsky
PyDinsky team repository for McGill Physics Hackathon 2020

## Why Pydinski
We're creating generative art with user input and elements of randomness. Our name is a play on [Wassily Kandinsky](https://en.wikipedia.org/wiki/Wassily_Kandinsky), a Russian painter who pioneered abstract art and used bold colors liberally in his work. Prior to Kandinsky's contributions to mainstream aesthetic theories, what we now call abstract art was rejected as a true art form. To this day, there is a stigma around abstract art. "What is up with that painting?", you might have heard, or "My three-year-old nephew could have painted this rubbish." This perspective misses a key aspect of art: what emotions do you feel when looking at a piece? Kandinsky argued that abstract art could be equally emotionally impactful as more representative works. He drew comparisons to other art forms, such as music, to argue that simple colors arranged in non-representative ways could move the viewer. Fortunately, paradigm shift has promoted the creation of abstract pieces all over the world, in a diverse and inclusive way. PyDinsky is our modest attempt to be part of this movement and hopefully, you, the viewer, will be moved by what you see here. 

## The Concept
The phenomena of heat diffusion is somewhat familiar to all. Indeed temperature fluctuations and "movement" is part of our everyday experience. A phenomena inheretly linked to temperature and diffusion is that of random walks. This is NOT a concept trivially known to all. With our project, we chose to represent artistically those aforementioned random walks on the stage of the earth. Their trajectories are based on the live local temperatures at different cities in the world. 

## The "Physics"
Every time you generate an image it will be different. We implemented random walk methods that follow a **Boltzmann distribution** and are seeded with a temperature from a given city. We plot the trace of walkers using a color scheme that matches the given temperature.

## Use your favorite cities to generate images
The color schemes used for the walkers are generated using the current temperature of the cities of your choice, pulled from the [OpenWeather](https://openweathermap.org/) API. A cold scheme for a colder day and a warm scheme for a blazing hot day.

Web app available at: https://pydinsky.herokuapp.com/main-bokeh

Welcome to the paartyyy

![](animation1.gif)![party time](https://github.com/soudk/PyDinsky/blob/main/data/animation1.gif?raw=true)


