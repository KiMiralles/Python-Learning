# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:59:54 2015

@author: Kike
"""

from math import pi
from numpy import linspace, sin, cos, exp
from pylab import plot, show

# For the Deltoid curve:

#values = linspace(0, 2*pi, 1000)

#x = 2*cos(values) + cos(2*values)
#y = 2*sin(values) - sin(2*values)
#
#plot(x,y)
#show()

# For the Galilean spiral:

#values = linspace(0, 10*pi, 1000)
#
#r = values**2
#
#x = r*cos(values)
#y = r*sin(values)
#
#plot(x,y)
#show()

# For Fey's function:

values = linspace(0, 24*pi, 1000)

r = exp(cos(values)) - 2*cos(4*values) + (sin(values/12))**5

x = r*cos(values)
y = r*sin(values)

plot(x,y)
show()