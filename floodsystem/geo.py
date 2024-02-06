# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy
from . import datafetcher
from .stationdata import build_station_list
from .station import MonitoringStation
import math
from haversine import haversine

def stations_by_distance(stations, p):
    station_dist = []
    for station in stations:
        dist = haversine(p[0], p[1], station.coord[0], station.coord[1])
        vals = station.name, station.town, dist
        station_dist.append(vals)
    stations_sorted = sorted_by_key(station_dist,2)
    
    return stations_sorted
1
