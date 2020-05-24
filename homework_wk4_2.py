# DO NOT EDIT THIS CODE
import pandas as pd
import numpy as np
birddata = pd.read_csv("https://courses.edx.org/asset-v1:HarvardX+PH526x+2T2019+type@asset+block@bird_tracking.csv", index_col=0)
birddata.head()


# Exercise 1
# First, use `groupby()` to group the data by "bird_name".
grouped_birds = birddata.groupby(["bird_name"])

# Now calculate the mean of `speed_2d` using the `mean()` function.
mean_speeds = grouped_birds.mean().speed_2d

# Find the mean `altitude` for each bird.
mean_altitudes = grouped_birds.mean().altitude

print(mean_altitudes)


# Exercise 2
# Convert birddata.date_time to the `pd.datetime` format.
# birddata.date_time = 

# Create a new column of day of observation
birddata["date"] = pd.to_datetime(birddata.date_time, format = '%Y-%m-%d').dt.strftime('%Y-%m-%d')

# Use `groupby()` to group the data by date.
grouped_bydates = birddata.groupby(["date"])

# Find the mean `altitude` for each date.
mean_altitudes_perday = grouped_bydates.mean().altitude

print(mean_altitudes_perday)



# Exercise 3
# Use `groupby()` to group the data by bird and date.
grouped_birdday = birddata.groupby(["bird_name", "date"])

# Find the mean `altitude` for each bird and date.
mean_altitudes_perday = grouped_birdday.mean().altitude

print(mean_altitudes_perday)


# Exercise 4
import matplotlib.pyplot as plt

grouped_birdday = birddata.groupby(["bird_name", "date"])
mean_speed_perday = grouped_birdday.mean().speed_2d

eric_daily_speed  = mean_speed_perday["Eric"]
sanne_daily_speed = mean_speed_perday["Sanne"]
nico_daily_speed  = mean_speed_perday["Nico"]

eric_daily_speed.plot(label="Eric")
sanne_daily_speed.plot(label="Sanne")
nico_daily_speed.plot(label="Nico")
plt.legend(loc="upper left")
plt.show()
