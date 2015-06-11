# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:20:55 2015

@author: Kike
"""

from numpy import loadtxt, sum
from pylab import plot, show

data = loadtxt("MovingAverageSample.txt", int)
years = data[:,0]
sales = data[:,1]

moving_average = []

for index in range(2,(len(sales)-2)):
    value = (1/5) * sum(sales[(index-2):(index+3)])
    print(value)
    moving_average.append(value)
reduced_years = years[2:-2]

plot(years, sales, "b-")
plot(reduced_years, moving_average, "g-")
show()