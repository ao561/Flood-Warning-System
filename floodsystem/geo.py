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
from math import radians, cos, sin, asin, sqrt

'''Task 1B'''

def haversine_formula(lon1, lat1, lon2, lat2):
    '''Standard Haversine formula function'''
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r


def stations_by_distance(stations, p):
    '''creates list of 10 closest and furthest stations'''
    station_dist = []
    for station in stations:
        dist = haversine_formula(p[0], p[1], station.coord[0], station.coord[1])
        vals = station.name, station.town, dist
        station_dist.append(vals)
    stations_sorted = sorted_by_key(station_dist,2)
    
    return stations_sorted



'''Task 1C'''
def stations_within_radius(stations, centre, r):
    stations_within_radius = []
    for station in stations:
        if (haversine(station.coord, centre) <= r):
            stations_within_radius.append(station.name)
    return stations_within_radius




'''Task 1D'''

def rivers_with_station(stations):
    '''creates list of stations without duplicates'''
    for station in stations:
        river_list = []
        for station in stations:

            if station.name != None:

                if station.river not in river_list:
                    river_list.append(station.river)
    return river_list



def stations_by_river(stations):
    '''creates dictionary of rivers and their respective stations'''
    river_dict = {}
    for a in stations:                               #iterates to get 1 river
        stations_in_river_list = []
        for b in stations:
            if a.river == b.river:                  #finds all the stations in that river 
                stations_in_river_list.append(b.name)
        
        river_dict[a.river] = stations_in_river_list         #appends each river
    
    return river_dict



'''Task 1E'''

def rivers_by_station_number(stations, N):
    '''creates list of rivers and respective number of stations'''
    river_dict = stations_by_river(stations)
    
    river_station_number = []

    for key in river_dict.keys():
        number_stations = len(river_dict[key])
        
        river_station_number.append(key, number_stations)




