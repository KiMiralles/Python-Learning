# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:35:59 2015

@author: Kike
"""

from pylab import plot, show, ylabel, xlabel,xlim
from numpy import loadtxt

data = loadtxt("sunspots.txt", float)
month = data[:,0]
sunspots = data[:,1]

running_average = []

r=5 # Range of the interval at each side of the central value.

for index in range(r,(len(sunspots)-r)):
    Y = sum(sunspots[index-5:index+6])/(2*r + 1)
    running_average.append(Y)
modified_month = month[r:-r]

plot(month, sunspots, "k-")
plot(modified_month, running_average, "r-")
xlabel("Time")
ylabel("Number of observed sunspots")
xlim(0,1000)
show()