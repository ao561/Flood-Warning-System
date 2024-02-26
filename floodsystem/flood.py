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
