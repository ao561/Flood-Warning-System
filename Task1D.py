from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    '''Build list of stations'''
    stations = build_station_list()

    river_stations = stations_by_river(stations)

    print(len(river_stations),"stations.")
    river_stations_sorted = river_stations.sort()

    print("First 10 -", river_stations_sorted[:10])
    
    

    


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()