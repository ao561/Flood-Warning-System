
import numpy
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations





'''Task 1B'''



'''Task 1C'''



'''Task 1D'''

def test_rivers_with_station():
    '''test for number of stations and making sure each river has at least one station'''
    stations = build_station_list()
    rivers_stations = rivers_with_station(stations)
    assert len(rivers_stations) == 1021
    for a in stations:
        for b in rivers_stations:
            n = 0

            if a.river == b:
                n = n + 1
                assert n >= 1


def test_stations_by_river():
    '''Test to see that stations in rivers dictionary lie on that river'''
    stations = build_station_list()
    station_dict = stations_by_river(stations)

    aire_station = station_dict["River Aire"]
    cam_station = station_dict["River Cam"]
    thames_station = station_dict["River Thames"]

    for a in stations:
        for k in aire_station:
            if a.name == aire_station:
                assert a.river == "River Aire"

        for l in cam_station:
            if a.name == cam_station:
                assert a.river == "River Cam"

        for m in thames_station:
            if a.name == thames_station:
                assert a.river == "River Thames"




'''Task 1E'''

def test_rivers_by_station_number():
    N = 9
    stations = build_station_list()
    test = rivers_by_station_number(station, N)
    assert len(test) >= 9




'''Task 1F'''