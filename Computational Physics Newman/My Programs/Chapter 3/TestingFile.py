# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 09:59:35 2015

@author: Kike
"""

from pylab import plot, show, ylim, xlabel, ylabel
from numpy import linspace, sin, cos, loadtxt

#x = linspace(0,10,100)
#y = sin(x)
#plot(x,y)
#show()

#data = loadtxt("Values.txt", float)
#x = data[:,0]
#y = data[:,1]
#plot(x,y)
#show()

x = linspace(0, 10, 100)
y1 = sin(x)
y2 = cos(x)
plot(x, y1, "k-")
plot(x, y2, "g--")
ylim(-1.1, 1.1)
xlabel("x axis")
ylabel("Dash: cos x // Solid: sin x")
show()