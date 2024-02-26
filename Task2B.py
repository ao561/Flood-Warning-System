from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    print("hello")
    '''# Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stations_level_over_threshold(stations, 0.8)
    '''

    '''for station in stations:
        if station.name in names:
            print("Station name and current level: {}, {}".format(
                station.name, station.latest_level))'''


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()