# EcoSentinel #

## Problem + Solution ##

Much like the Lorax, we are here to guard the trees.

Currently, there exists no standardized method of measuring ecological damage across the world. More importantly, there exists no simple way to broadcast important information in a form that is easily accessible and digestible. EcoSentinel serves as an independent, AI powered monitor that analyzes Google Earth data into an intermediary dataset (presented as a map of deforestation). EcoSentinel then conducts further time-series analysis on this dataset to calculate risk of ecological systems and then assign grades to countries based on their success in preventing ecological loss.

Ecosentinel solves this in two two key areas: Measurement and Analytics.

### Measurement ###
The measurement of the impact of any efforts, initiatives, etc. that are being implemented by governments in hopes of obtaining and broadcasting information.

We can evaluate the effectiveness of certain methods of combating climate change and deforestation. This can be built upon to eventually conduct predictive analytics to gauge effectiveness prior to even executing a plan. 

Additionally, governments can get an idea of the impact they have on the progress of climate change. They can then use the data and predictions gathered to influence lawmaking and other legislative agendas/decisions. The same concept could also apply to companies, though targeting company efforts becomes much more complicated and may be developed in future iterations.

Arguably the most important impact is people can understand the weight of the problem easier (how much damage there is, but also how reliable some solutions can be). This could materialize as us potentially serving as an unbiased, third-party “watchdog” or tracker of ecological damage so everyone can understand who is contributing to what damage. Since the whole process (from algorithms to datasets we generate) is transparent to the public, there is a level of trust present in the launching of EcoSentinel.

### Analytics ###
The conducting of post-generative analytics to predict the progress of climate change, especially with respect to specific areas and governments.

We can keep a list of countries/regions to watch out for given the rate of damage as well as historical data (both information that we generate in our tracking, as well as information available prior to our tracker being implemented).

Essentially, we track damage with computer vision on Google Earth data and then conduct analysis on the data we ourselves have generated.

## Issues Targeted ##

In terms of which of the UN’s goals are being targeted, we believe it will help with:

#### Goal 9: Industry, Innovation and Infrastructure ####
We use effectively the same reasoning as goal 11, iffy whether or not it counts but we figure the end-goal of forwarding the economy sustainably allows us to count this.
    
#### Goal 11: Sustainable Cities and Communities #### 
We’re providing the insights necessary for governments to implement more sustainable building/expansion practices.
        
We can provide predictive analytics to weigh the effects of certain expansion practices (what expanding into a certain natural ecosystem might do to affect that ecosystem). We can also Provide the data necessary to gauge which ecosystems are most at risk and therefore will require a ban in expansion into those spaces.

#### Goal 12: Responsible Consumption and Production ####
We can act as a regulatory body by providing insights to companies on the impacts of their materials sourcing on ecological systems.

By implementing a system in which certain companies & countries receive a grade based on how well they are taking care of their natural ecosystems and contributing to the world’s fight against climate change (both good and bad contributions will be weighted), we incentivize the public to get involved in helping their country be a better role model.

#### Goal 13: Climate Action #### 
This goal is very closely tied in with the whole project: we’re aiming to give people the information & insights necessary to take action themselves.

In other words, we’re giving everyone the resources to create positive change since the limits of AI constrain us from physical action (without robotics, of course).

#### Goal 15: Life on Land ####
This goal is closely tied in with all the previous goals’ reasoning.

## Deliverables ##

### Ecosystem AI ###
Maps a square unit of Earth's surface to a type of region, allowing us to generate a 3D model of the Earth’s ecological and human systems.

If there is a Google alternative to what Bing has already done (with mapping all the trees in the world), we can also do that to avoid mapping ecosystems and instead track deforestation.

### Web App ###
Allows users to access a rudimentary 3D model that is pre-rendered each day on a cloud server.

Additionally, if there are specific regions to watch out for (such as during a wildfire, the amazon, etc.), we can more frequently update those as needed. Additional processing will be needed to determine this.

### Earth Visualization ####
Given the augmented data that the Ecosystem AI will produce, we should be able to generate a rough 3D model of either the trees on Earth or a color-gradient map that shows areas of high damage vs low damage in comparison to previous years.

This deliverable is the most important for broadcasting information to the public in a digestable way. Visuals must be made (and presented on the web app) in a way that is easily understood by the general public and highlights high-risk areas and low-effort governments.

### Post-Generation Analytics ###
Given the data from the Forest AI, we should be able to calculate the risk of certain areas being impacted beyond repair.

+ This risk factor should be another color-gradient shown in the 3D model
- Risk factor should take in the following features:
    - Number of cities in the surrounding area (~50 miles from a given tree/data point)
    - Population of cities in the surrounding area (~50 miles from a given tree/data point)
    - Recent trends in damage (in the last ~3 years)
    - Current deforestation percentage (can be retrieved from another dataset probably)

Future iterations can add other analysis that determines insights (near a city means that city is likely causing damage, near a farm means grazin or slash/burn techiques might be the cause, etc.).

## Concerns ##
The amount of processing needed to generate a model and identify billions of trees around the Earth may force us to narrow our outlook to just a few key regions on Earth (Amazon rainforest, national parks in the US, etc.)

The amount of data needed to accomplish the project will be high, we should focus on doing one step at a time instead of overloading what we can possibly do in the timeframe