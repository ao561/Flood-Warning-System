from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)


    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
        datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
        datetime(2017, 1, 5)]
    level = [0.2, 0.7, 0.95, 0.92, 1.02, 0.91, 0.64]

    # Plot
    plt.plot(t, level)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station A")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()