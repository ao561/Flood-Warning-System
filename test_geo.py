
import numpy
from floodsystem.geo import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius



'''Task 1B'''

def test_stations_by_distance():
  stations = build_station_list()
  distances = stations_by_distance(stations, p=[0,0])
  for i in range(1, len(distances)):
      d1 = distances[i]
      d2 = distances[i-1]
      assert d1[2] >= d2[2]

'''Task 1C'''

def test_stations_within_radius():
  stations = build_station_list()
  coordinate = (52.2053, 0.1218)
  stations_within_range = stations_within_radius(stations, coordinate,10)
  for i in stations:
      for j in stations_within_range:
          if i.name == j:
              assert haversine(coordinate, i.coord) <= 10


'''Task 1D'''

def test_rivers_with_station():
    '''test for number of stations and making sure each river has at least one station'''
    stations = build_station_list()
    rivers_stations = rivers_with_station(stations)
    assert len(rivers_stations) == 1025
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
    station = build_station_list()
    test = rivers_by_station_number(station, N)
    assert len(test) >= 9


'''Task 1F'''
def test_inconsistent_typical_range_stations():
  stations = build_station_list()
  inconsistent_stations = inconsistent_typical_range_stations(stations)
  for i in stations:
      for j in inconsistent_stations:
          if i.name == j:
              assert i.typical_range == None or i.typical_range[1] - i.typical_range[0] < 0