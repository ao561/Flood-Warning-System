from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta


def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)
    severe_stations = stations_level_over_threshold(stations, 1.6)
    station_data = []

    for station in stations:
        if station.name in severe_stations:
            station_data.append(station)
    
    for station in station_data:
        assert station.latest_level > station.typical_range[1] 
