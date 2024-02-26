from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.plot import plot_water_levels
def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    threshold_list = stations_highest_rel_level(stations, 5)
    names = []
    for i in range(len(threshold_list)):
        names.append(threshold_list[i][0])
    
    for i in stations:
        for a in names:
            if a == i.name:
                dates, levels = fetch_measure_levels(i.measure_id, dt=timedelta(days = 10))
                plot_water_levels(i, dates, levels)

    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()