import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta, date, time
from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list
from .analysis import polyfit

def plot_water_levels(station, dates, levels):

    t = dates
    level = levels

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Stations {}".format(station.name))

    plt.axhline(y=station.typical_range[0],linestyle ='--')
    plt.axhline(y=station.typical_range[1],linestyle ='--')

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates, levels, 'r')
    plt.plot(dates, poly, 'b')
    for i,j in zip(dates, levels):
        if j == station.typical_range[0]:
            plt.plot(i, j, marker='o', color='green')
        elif j == station.typical_range[1]:
            plt.plot(i, j, marker='*', color='green')
    plt.xlabel("Date")
    plt.ylabel("Water Level")
    plt.xticks(rotation = 45)
    plt.title("Station {}".format(station.name))
    plt.show()




