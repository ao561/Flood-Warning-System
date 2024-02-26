# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        if self.typical_range is None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True

'''Task 1F'''

def inconsistent_typical_range_stations(stations):
    inconsistent_data_stations = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) is False:
            inconsistent_data_stations.append(station)
        else:
            pass
    return inconsistent_data_stations


'''Task 2B'''

def relative_water_level(self, latest_level):
    a = self.typical_range is not None and float(self.typical_range[1] - self.typical_range[0]) >= 0               #makes sure range is correct
    if a == True: 
        if latest_level is not None:
            x = (float(latest_level - self.typical_range[0]) / (float(self.typical_range[1] - self.typical_range[0])))
            return x
        elif latest_level is None:
            return None
    

