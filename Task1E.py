from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station


def run():
    '''Build list of stations'''
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    print(len(rivers),"stations.")

    rivers.sort()
    print("First 10 -", rivers[:10])

    river_dict = stations_by_river(stations)

    print("\nRiver Aire stations:", sorted(river_dict["River Aire"]))
    print("\nRiver Cam stations:", sorted(river_dict["River Cam"]))
    print("\nRiver Thames stations:", sorted(river_dict["River Thames"]))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
