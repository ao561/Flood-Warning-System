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





if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

