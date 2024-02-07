from .utils import sorted_by_key  # noqa
import numpy
from . import datafetcher
from .stationdata import build_station_list
from .station import MonitoringStation
import math
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations






'''Task 1B'''



'''Task 1C'''



'''Task 1D'''

def test_rivers_with_station():
    stations = build_station_list()
    r = rivers_with_station(stations)
    assert len(r) == 857
    for i in stations:
        for j in r:
            a = 0
            if i.river == j:
                a = a+1
                assert a>= 1

'''Task 1E'''



'''Task 1F'''