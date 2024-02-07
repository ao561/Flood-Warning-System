

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    cam_city_centre_coordinate = (52.2053, 0.1218)
    stations_within_radius_sorted = sorted(stations_within_radius(stations, cam_city_centre_coordinate, 10))
    print(stations_within_radius_sorted)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

