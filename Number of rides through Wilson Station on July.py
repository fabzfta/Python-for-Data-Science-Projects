#In this exercise we have to find the number os passangers that traveled by Chicago's public transportation through Willson station during all weekdays on July.
#We use three different databases: cal, ridership and stations DataFrames

import pandas as pd

# Merging the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
							.merge(stations, on='station_id')

# Creating a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7)
                   & (ridership_cal_stations['day_type'] == "Weekday")
                   & (ridership_cal_stations['station_name'] == "Wilson"))

# Using .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# 140005 Passengers.
