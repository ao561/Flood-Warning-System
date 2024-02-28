import analysis
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import numpy as np

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
    x = mdates.date2num(dates)

    plt.plot(dates, levels, 'b.', label = 'Water Levels')
    x_test = np.linspace(x[0], x[-1], 100)

    test_dates = mdates.num2date(x_test)

    plt.plot(test_dates, poly(x_test -x[0]), 'r-', label = "Best-fit Polynomial (Degree{})".format(p))

    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation = 45)

    # Typical high and low values

    plt.axhline(station.typical_range[0], color = 'r', label = 'Typical Low')
    plt.axhline(station.typical_range[1], color = 'b', label = 'Typical High')

    plt.title(station.name)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show






