
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
    assert len(r) == 1012
    for a in stations:
        for b in rivers_stations:
            n = 0
            if a.river == j:
                n = n + 1
                assert n >= 1




'''Task 1E'''



'''Task 1F'''