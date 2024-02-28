from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level



stations = build_station_list()
update_water_levels(stations)


def test_stations_level_over_threshold():
    tol = 0.8
    threshold_stations = stations_level_over_threshold(stations, tol)
    for i in stations:
        for j in threshold_stations:
            if j[0] == i.name:
                assert j[1] > 0.8



def test_stations_highest_rel_level():
    N = 5
    threshold_stations = stations_highest_rel_level(stations, N)
    
    assert len(threshold_stations) == N
    
    for i in range(N-1):
        assert threshold_stations[i][1] >= threshold_stations[i+1][1]






