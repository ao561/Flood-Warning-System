import unittest
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.analysis import polyfit

class TestPolyfitFunction(unittest.TestCase):

    def test_polyfit(self):
        # Example data
        dates = [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)]
        levels = [1.0, 2.0, 3.0]
        degree = 2

        # Call the polyfit function
        result, dates_shifted = polyfit(dates, levels, degree)

        # Check if the result is a list
        self.assertIsInstance(result, list)

        # Check if the length of the result is the same as the input dates
        self.assertEqual(len(result), len(dates))

        # Check if dates_shifted is a list and has the correct values
        self.assertIsInstance(dates_shifted, list)
        self.assertEqual(dates_shifted, [0.0, 1.0, 2.0])

if __name__ == '__main__':
    unittest.main()