from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels

from datetime import datetime, timedelta, date, time
import datetime

import io
import pygame as pg
import time
import requests
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen



def risk_criterion_analyser(tol, days):
    stations = build_station_list()
    update_water_levels(stations)
    a = stations_level_over_threshold(stations, tol)
    m = []
    for i in a:
        m.append(i[0])

    for i in stations:
        for name in m:
            if name == i.name:
                lol = []
                for k in fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[1]:
                    p = (float(k) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol.append(p)
                plot_water_levels(i, fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[0], lol)
    mean_list = []

    for i in stations:
        for name in m:
            if name == i.name:
                lol2 = []
                L = 0
                lol3 = []
                L2 = 0
                for k in fetch_measure_levels(i.measure_id, dt = timedelta(days = 10000))[1]:
                    p = (float(k) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol2.append(p)
                    if p > 1.2: #1.2 times relative typical high
                        L += 1
                        lol3.append(p)
                        summation = 0
                        for member in lol3:
                            summation += member
                if L != 0:
                    mean = summation / L # Mean of all relative water level values which are greater than 1.2
                    mean_list.append(mean)
                lol4 = []
                L3 = 0
                lol5 = []
                L4 = 0
                for k2 in fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[1]:
                    p2 = (float(k2) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol4.append(p2)
                    if p2 > 1.5 * mean: # Caution if water level is greater than 1.5 times mean for an extended cumulative period of time
                        L3 += 1
                print(L3)
                if L3 > 25*days:
                    print("Severe Risk of Flooding for Station {}".format(i.name))
                elif 25*days >= L3 > 10*days:
                    print("High Risk of Flooding for Station {}".format(i.name))
                elif 10*days >=  L3 > 5*days:
                    print("Moderate Risk of Flooding for Station {}".format(i.name))
                elif L3 <= 5*days:
                    print("Low Risk of Flooding for Station {}".format(i.name))

    print(mean_list)

    return


def run():
    
    print(risk_criterion_analyser(1.2, 10))

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
