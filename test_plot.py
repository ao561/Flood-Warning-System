from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_plot(plot_water_levels):
    stations = build_station_list()
    update_water_levels(stations)
    plot_water_levels.assertRaises(IndexError, plot_water_levels, stations, [1, 2], [2])

    
