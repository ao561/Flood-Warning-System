from .utils import sorted_by_key  # noqa
from .stationdata import build_station_list
from .station import MonitoringStation
from .stationdata import update_water_levels

'''Task 2B'''

def stations_level_over_threshold(stations, tol):
    threshold_stations = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level(station.latest_level) is not None and station.relative_water_level(station.latest_level) > tol:
            station_water_level_name = station.name, station.relative_water_level(station.latest_level)
            threshold_stations.append(station_water_level_name)
        
    sorted_threshold_stations = sorted_by_key(threshold_stations, 1, reverse=True)
    return sorted_threshold_stations

'''Task 2C'''

def stations_highest_rel_level(stations, N):
    station_list = []
    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            station_water_level_name = station.name, station.relative_water_level(station.latest_level)
            station_list.append(station_water_level_name)
    sorted_station_list = sorted_by_key(station_list, 1, reverse=True)
    cut_sorted_station_list = sorted_station_list[:N]
    return cut_sorted_station_list