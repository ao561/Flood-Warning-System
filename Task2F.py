import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

stations = build_station_list()
update_water_levels(stations)
high_stations = stations_highest_rel_level(stations, 5)
dt = 2
station_data = []
high_station_names = [x[0] for x in high_stations]

p = 4

for station in stations:
    if station.name in high_station_names:
        station_data.append(station)
for station in station_data:
    try:
        data = fetch_measure_levels(station.measure_id, dt = datetime.timedelta(days=dt))
        dates = data[0]
        levels = data[1]
        plot_water_level_with_fit(stations, dates, levels, p)
    except KeyError:
        dt = dt-1
        data = fetch_measure_levels(stations.measure_id, dt = datetime.timedelta(days=dt))
        levels = data[1]
        dates = data[0]
        plot_water_level_with_fit(station,dates,levels, p)




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
    