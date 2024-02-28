'''from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_plot(plot_water_levels):
    stations = build_station_list()
    update_water_levels(stations)
    plot_water_levels.assertRaises(IndexError, plot_water_levels, stations, [1, 2], [2])

    

# Task 2F

import unittest
import matplotlib.pyplot as plt
from datetime import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import Station, TypicalRange
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from matplotlib.testing.decorators import cleanup

class TestPlotWaterLevelWithFit(unittest.TestCase):

    def setUp(self):
        # Create a sample station for testing
        self.sample_station = Station("Test Station", "Station_ID", (0.0, 1.0), TypicalRange(2.0, 3.0))

    @cleanup
    def test_plot_water_level_with_fit(self):
        # Example data
        dates = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
        levels = [1.0, 2.0, 3.0]
        degree = 2

        # Call the plot_water_level_with_fit function
        plot_water_level_with_fit(self.sample_station, dates, levels, degree)

       
        
        plt.savefig('test_plot.png')
        elf.assertImagesSimilar('test_plot.png', 'expected_plot.png', tol=1e-3)

if __name__ == '__main__':
    unittest.main()

import unittest
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels, plot_water_level_with_fit

FakeA = MonitoringStation("fakea", "fakemeasurea", "A", (0, 10), (-1, 100), "River A", "Town A")

FakeList = [FakeA]

class TestCase(unittest.TestCase):
    def test_plot_water_levels(self):
        self.assertRaises(IndexError, plot_water_levels, FakeList, [1, 2], [2])
        self.assertRaises(IndexError, plot_water_levels, FakeList, [1], [2, 3])
        
    def test_plot_water_level_with_fit(self):
        self.assertRaises(IndexError, plot_water_level_with_fit, FakeList, [1, 2], [2], 3)
        self.assertRaises(IndexError, plot_water_level_with_fit, FakeList, [1], [2, 3], 3) '''


from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels
from floodsystem.stationdata import build_station_list

def test_plot_water_level_with_fit():
    stations = build_station_list()
    update_water_levels(stations)
    severe_stations = stations_level_over_threshold(stations, 1.6)
    station_data = []

    for station in stations:
        if station.name in severe_stations:
            station_data.append(station)
    
    for station in station_data:
        assert station.latest_level > station.typical_range[1]
