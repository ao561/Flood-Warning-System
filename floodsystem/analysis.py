import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def polyfit(dates, levels, p):
    m = mdates.date2num(dates)
    p_coeff = np.polyfit(m-m[0], levels, p)
    poly = np.poly1d(p_coeff)
    d0 = dates[0]
    return poly, d0